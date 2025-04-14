#!/bin/python
# for a csv file of compounds, get one html that lists all EICs and EIMs next to each other

import sys
import pandas as pd
import holoviews as hv
from holoviews import opts
from getFunctions import *

# Check for correct number of arguments
if len(sys.argv) < 3:
    print("Usage: python EIC_EIM_plotting.py <input.csv> <input.d> <output.html>")
    sys.exit(1)

input_csv = sys.argv[1]
bruker_file = sys.argv[2]
output_html = sys.argv[3]

# read in suspect list
suspect = pd.read_csv(input_csv, header=0)

# read in data 
data = alphatims.bruker.TimsTOF(bruker_file)

# get graphs
plots_list = []
for index, row in suspect.iterrows():
    print(row.iloc[0])
    eic = (getEIC(file=data, mz=float(row.iloc[1]), name=row.iloc[0], rt=row.iloc[2], rt_tol=1, im=row.iloc[3], im_tol=0.5, ppm=5
                 )* hv.VLine(row.iloc[2])).opts(opts.VLine(color='red')) 
    eim = (getEIM(file=data, mz=float(row.iloc[1]), name=row.iloc[0], rt=row.iloc[2], rt_tol=0.1, ppm=5
                  )* hv.VLine(row.iloc[3])).opts(opts.VLine(color='red'))
    dmap = (getMap(file=data, mz=float(row.iloc[1]), rt=row.iloc[2], rt_tol=1, im=row.iloc[3], im_tol=0.5, ppm=5))
    plots_list.append(eic + eim + dmap)

# plot graphs in html
hv.save(hv.Layout(plots_list).opts( opts.Layout(shared_axes=False)).cols(3), output_html, backend="bokeh")

