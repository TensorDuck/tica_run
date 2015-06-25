"Useful universal methods for using TICA on NMDA"

import numpy as np
import matplotlib.pyplot as plt

def generate_pairs(start, stop, step, cut):
    pair = []
    for i in np.arange(start, stop, step):
        for j in np.arange(i+cut, stop, cut):
            pair.append([i, j])
    
    pairs = np.array(pair)
        
    return pairs

def plot_time_lag_series(data, time_scale, title, axis=None):
    plt.figure()
    
    time_lags = data[:,0]
    eigenvalue = data[:,1]
    ##multiply in time_lags information for the scale
    try:
        time_lags *= time_scale
        unit_string = "ns"
    except:
        unit_string = "arb"
    test = np.array([eigenvalue<0])
    if not test.any():
        time_ratio = np.log(eigenvalue)
    else:
        time_ratio = np.log(np.abs(eigenvalue))
        for idx, ev in enumerate(eigenvalue):
            if not ev > 0:
                time_ratio[idx] = -time_ratio[idx]
    eigen_time_scale = -1.0 / time_ratio 
    eigen_time_scale *= time_lags
    plt.figure()
    plt.plot(time_lags, eigen_time_scale, 'ok')
    plt.xlabel("Time Lag (%s)"%unit_string, fontsize=20)
    plt.ylabel("Time scale (%s)"%unit_string, fontsize=20)
    if not args.axis == None:
        plt.axis(args.axis)
    plt.savefig("%s" %title)
    plt.show()
    
    
def plot_eigen_series(eigenvalue, title, time_scale=None, axise=None, axist=None):
    #eigenvalues is a 1-D array
    #time_scale is the lag time used for this data in ns
    
    #First plot the eigenvalues in sequence:
    plt.figure()
    
    plt.plot(np.arange(0, np.shape(eigenvalue)[0]), eigenvalue, 'ok')
    plt.xlabel("EigenNumber", fontsize=20)
    plt.ylabel("Eigenvalue", fontsize=20)
    
    if axise == None:
        plt.axis([0, np.shape(eigenvalue)[0] + 0.5, np.min(eigenvalue)-0.1, 1.1])
    else:
        plt.axis(axise)
    plt.savefig("%s_eigenvalue.png" %title)
    
    
    
    ##multiply in time_lags information for the scale
    if time_scale == None:
        unit_string = "ns"
    else:
        unit_string = "arb"
    test = np.array([eigenvalue<0])
    if not test.any():
        time_ratio = np.log(eigenvalue)
    else:
        time_ratio = np.log(np.abs(eigenvalue))
        for idx, ev in enumerate(eigenvalue):
            if not ev > 0:
                time_ratio[idx] = -time_ratio[idx]
    eigen_time_scale = -1.0 / time_ratio 
    eigen_time_scale *= time_scale
    plt.figure()
    plt.plot(np.arange(0, np.shape(eigenvalue)[0]), eigen_time_scale, 'ok')
    plt.xlabel("EigenNumber", fontsize=20)
    plt.ylabel("Time scale (%s)"%unit_string, fontsize=20)
    maxvalue = np.max(eigen_time_scale)
    minvalue = np.min(eigen_time_scale)
    diff = maxvalue - minvalue
    if axist == None:
        plt.axis([0, np.shape(eigenvalue)[0] + 0.5, minvalue-(diff*0.1), maxvalue+(diff*0.1)])
    else:
        plt.axis(axist)
    plt.savefig("%s_timescale.png" %title)
    plt.show()

def plot_output(outputs, title, time_scale=None):
    if time_scale == None:
        unit_string = "ns"
        time_value = np.arange(0, np.shape(outputs)[0])*time_scale
    else:
        unit_string = "arb" 
        time_value = np.arange(0, np.shape(outputs)[0])
        
    for i in xrange(np.shape(outputs)[1]):
        plt.figure()
        plt.plot(time_value, outputs[:,i])
        plt.xlabel("Time (%s)"%unit_string, fontsize=20)
        plt.ylabel("TICA value", fontsize=20)
        plt.title("TICA Eigenvalue %d" % i, fontsize=20)
        plt.savefig("%s_output_%d.png" %(title, i))
  
        
    
    
    
    
    
    
    
    
    
    
    



