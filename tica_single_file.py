""" 
For performing a single TICA run and outputting the desired files. 
"""

import numpy as np
import mdtraj as md
import time
import argparse
try:
    import pyemma
    import pyemma.coordinates as coor
except:
    print "pyemma not imported!"

import analysis_scripts.plot_package as pltpkg
import tica_run.tica_methods as tmeth

def run_analysis(args):
    feat = coor.featurizer(args.topfile)
    feat.add_distances(tmeth.generate_pairs(args.range[0],args.range[1], args.step_size, args.cut_value))
    traj = coor.load(args.traj_file, feat, stride=args.stride)
    tica_obj = coor.tica(traj, stride=1, lag=args.lag, dim=args.ticadim)
    outputs = tica_obj.get_output()[0]
    eigen = tica_obj.eigenvalues
    np.savetxt("%s_output_raw.dat"%args.title, outputs)
    np.savetxt("%s_eigenvalues_raw.dat"%args.title, eigen)
    tmeth.plot_eigen_series(eigen, args.title, time_scale=args.time_step*args.stride)
    tmeth.plot_output(outputs, args.title, time_scale=args.time_step*args.stride)


def get_args():
    parser = argparse.ArgumentParser(description="parent set of parameters", add_help=False)
    parser.add_argument("--traj_file", type=str, help="Location of all xtc files")
    parser.add_argument("--topfile", type=str, help="top file for analysis")
    parser.add_argument("--range", default=[5,288], type=int, nargs = 2, help="specify range of contats to be fit")
    parser.add_argument("--step_size", default=4, type=int, help="Specify how far you want to step on the residues")
    parser.add_argument("--cut_value", default=4, type=int, help="Specify by what increment of residues you go by")
    parser.add_argument("--lag", default=1, type=int)
    parser.add_argument("--stride", default =1, type=int) 
    parser.add_argument("--ticadim", default=10, type=int, help="Number of TICA dimensions to save")
    parser.add_argument("--title", default="TICA-run", type=str, help="Save title")
    parser.add_argument("--time_step", default=0.0005, type=float, help="Time step of the whole trajectory")
    args = parser.parse_args()
    
    return args
    

if __name__ == "__main__":
    args = get_args()
    run_analysis(args)
