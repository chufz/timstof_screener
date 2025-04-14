import alphatims.bruker
import alphatims.plotting
import holoviews as hv

def getEIC(
        file, 
        mz, 
        ppm = 5,
        rt = 10,
        rt_tol = 10,
        im = 1,
        im_tol = 0.7,
        name = ''
):
    """Extracted ion chromatogram of one Bruker timstof file

    Args:
        file (alphatims object): Timstof Bruker *.d file
        mz (float): mz value to extract
        ppm (int, optional): mass window given in ppm. Defaults to 5
        rt (float, optional): rt value in min, Defaults to 10
        rt_tol (float, optional): rt plus minus tolerance in min, Defaults to 10
        im (float, optional): inverse ion mobility, Defaults to 1
        im_tol (float, optional): inverse ion mobility window, Defaults to 0.7
        name (string, optional): label
    """
    mz_slice = slice(
        mz / (1 + ppm / 10**6),
        mz * (1 + ppm / 10**6)
    )

    rt_slice = slice(
        float((rt - rt_tol) * 60),
        float((rt + rt_tol) * 60)
    )

    im_slice = slice(
        im - im_tol,
        im + im_tol
    )

    precursor_indices = file[
        rt_slice, # rt slot
        im_slice, # im slot
        0, #index 0 means that the quadrupole is not used
        mz_slice,
        "raw"
    ]

    xic = alphatims.plotting.line_plot(
            file,
            precursor_indices,
            x_axis_label="rt",
            width=350,
            remove_zeros=True,
            title=name
        )
    
    return xic

def getEIM(
        file, 
        mz, 
        ppm = 5,
        rt = 10,
        rt_tol = 10,
        im = 1,
        im_tol = 0.7,
        name = ''
):
    """Extracted ion mobilogram of one Bruker timstof file

    Args:
        file (alphatims object): Timstof Bruker *.d file
        mz (float): mz value to extract
        ppm (int, optional): mass window given in ppm. Defaults to 5
        rt (float, optional): rt value in min, Defaults to 10
        rt_tol (float, optional): rt plus minus tolerance in min, Defaults to 10
        im (float, optional): inverse ion mobility, Default to 1
        im_tol (float, optional): inverse ion mobility window, Defaults to 0.7
        name (string, optional): label
    """
    mz_slice = slice(
        mz / (1 + ppm / 10**6),
        mz * (1 + ppm / 10**6)
    )

    rt_slice = slice(
        float((rt - rt_tol) * 60),
        float((rt + rt_tol) * 60)
    )

    im_slice = slice(
        im - im_tol,
        im + im_tol
    )

    precursor_indices = file[
        rt_slice, # rt slot
        im_slice, # im slot
        0, #index 0 means that the quadrupole is not used
        mz_slice,
        "raw"
    ]

    xim = alphatims.plotting.line_plot(
            file,
            precursor_indices,
            x_axis_label="mobility",
            width=350,
            remove_zeros=True,
            title=name
        )
    
    return xim

def getMap(
        file,
        mz,
        ppm = 5,
        rt = 10,
        rt_tol = 10,
        im = 1,
        im_tol = 0.7,
        name = ''
):
    """Heatmap of a extracted mz value of one Bruker timstof file

    Args:
        file (alphatims object): Timstof Bruker *.d file
        mz (float): mz value to extract
        ppm (int, optional): mass window given in ppm. Defaults to 5
        rt (float, optional): rt value in min, Defaults to 10
        rt_tol (float, optional): rt plus minus tolerance in min, Defaults to 10
        im (float, optional): inverse ion mobility, Defaults to 1
        im_tol (float, optional): inverse ion mobility window, Defaults to 0.7
        name (string, optional): label
    """
    mz_slice = slice(
        mz / (1 + ppm / 10**6),
        mz * (1 + ppm / 10**6)
    )

    rt_slice = slice(
        float((rt - rt_tol) * 60),
        float((rt + rt_tol) * 60)
    )

    im_slice = slice(
        im - im_tol,
        im + im_tol
    )

    heatmap = alphatims.plotting.heatmap(
    file[rt_slice, im_slice, 0, mz_slice],
    x_axis_label="rt",
    y_axis_label="mobility",
    title=file.sample_name,
    width=350
    )

    return heatmap    

def getMS2(
         file,
         mz,
         ppm = 5,
         rt = 10,
         rt_tol = 10,
         im = 1,
         im_tol = 0.,
         name = "" 
):
    
    """ Get a PASEF dd-Spectra of a precursor mass of interest

    Args:
        file (alphatims object): Timstof Bruker *.d file
        mz (float): precursor mz value to extract
        ppm (int, optional): mass window given in ppm. Defaults to 5
        rt (float, optional): rt value in min, Defaults to 10
        rt_tol (float, optional): rt plus minus tolerance in min, Defaults to 10
        im (float, optional): inverse ion mobility, Defaults to 1
        im_tol (float, optional): inverse ion mobility window, Defaults to 0.7
        name (string, optional): label
    """

    rt_slice = slice(
        float((rt - rt_tol)*60),
        float((rt + rt_tol)*60)
    )
    im_slice = slice(
        im - im_tol,
        im + im_tol
    )
    precursor_mz_slice = slice(
        mz / (1 + ppm / 10**6),
        mz * (1 + ppm / 10**6)
    )

    fragment_indices = file[
            rt_slice,
            im_slice,
            precursor_mz_slice,
            :,
            "raw"
            ]

    p = alphatims.plotting.line_plot(file,
                             fragment_indices,
                             x_axis_label="mz",
                             width=900,
                             title=name)
    return p
