# timstof_screener
Code for fast extraction of extracted ion chromatograms (EICs) and extracted ion mobilograms (EIMs) for a list of compounds of intrest in Timstof data (Bruker *.d files). The code is relying on a installation of the alphatims package (see https://github.com/MannLabs/alphatims for further details).

# Requirements
We recommend using conda for a clean package environment. Install alphatims using the installation instructions (see https://github.com/MannLabs/alphatims for further details).

# Get a html with EICs and EIMs of a compound
We provide some testdata in the ´test` folder. The IS.csv contains a list of suspect m/z values, retention times and mobility values (as reduced mobility values 1/K_0) which should be plotted.

On the command line, run the following command:

```
python EIC_EIM_plotting.py test/IS.csv test/testfile.d test_output/IS_output.html
```







