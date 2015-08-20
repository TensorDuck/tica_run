import numpy as np
try:
    import pyemma
    import pyemma.coordinates as coor
except:
    print "pyemma not imported!"
import mdtraj as md
import time
import analysis_scripts.plot_package as pltpkg


if __name__ == "__main__":
    topology = "firstframe.pdb"
    feat = coor.featurizer(topology)
    
    pairs = np.array([[79,492]])

    feat.add_distances(pairs)
    
    print feat.describe()
    files_list = []
    for i in np.arange(0, 10, 1):
        files_list.append("ww_2-protein-00%d.dcd"%i)
    for i in np.arange(10, 50, 1):
        files_list.append("ww_2-protein-0%d.dcd"%i)
    
    output = coor.load(files_list, features=feat)
    
    print np.shape(output)
    
    yvalues = np.array(output).flatten()
    
    print np.shape(yvalues)
    
    np.savetxt("trace_ww_2.dat", yvalues)
    
    print np.max(yvalues)
    print np.min(yvalues)
    
