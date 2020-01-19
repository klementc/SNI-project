import random
import numpy as np
import sys, getopt
from math import log
import CoreSim as cs
from collections import deque


import MM1
import MMinf

if __name__ == "__main__":
    params = sys.argv[1:]
    if len(params) != 6:
        print("\n --- Usage: %s  mtba  mst  T  seed K N\n" % sys.argv[0])
        exit(0)
    else:
        mtba = float(sys.argv[1])	# mean time between arrivals
        mst = float(sys.argv[2])		# mean service time
        T = float(sys.argv[3])			# total simulation time
        seed = int(sys.argv[4])		# seed for the pseudo-r.n.
        K = int(sys.argv[5])
        N = int(sys.argv[6])
        
    np.random.seed(seed)
    seedStart=seed
    for i in range(seedStart, seedStart+N):
        print("exp number "+str(i))
        print(MM1.sim_mm1(mtba,mst,T,i,K))
        print(MMinf.sim_mminf(mtba,mst,T,i,K))
