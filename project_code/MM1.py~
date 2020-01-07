#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SNI 2019 - file MM1.py
"""
import random
import numpy as np
import sys, getopt
from math import log
import CoreSim as cs

def expo(mean):
    return -mean*log(np.random.random_sample())

arr = 1		# event-class: arrivals
dep = 2		# event-class: departures

if __name__ == "__main__":
    params = sys.argv[1:]
    if len(params) != 4:
        print("\n --- Usage: %s  mtba  mst  T  seed\n" % sys.argv[0])
        exit(0)
    else:
        mtba = float(sys.argv[1])	# mean time between arrivals
        mst = float(sys.argv[2])		# mean service time
        T = float(sys.argv[3])			# total simulation time
        seed = int(sys.argv[4])		# seed for the pseudo-r.n.
        print("\n --- Data: mtba = %.1f, mst = %.1f, T = %.1f, seed = %d" % (mtba,mst,T,seed))


# --- first operations on the scheduler

EvL = cs.LinkedList(T)	# --- end of simulation at time T

t = expo(mtba)
ev = cs.CREATE_EV(t,arr)
EvL.InsertEv(ev)	# --- first arrival at time t

t = t + expo(mst)
ev = cs.CREATE_EV(t,dep)
EvL.InsertEv(ev)	# --- first departure at time t

# --- initializing main variables
s = 0.0
nbUnits = 0
t_old = 0.0
t_next_arr = 0.0

nclass = -1
### --- central simulation loop
while nclass != cs.END_SIM:
    time, nclass = EvL.FirstEv()
    # ----------
    if nclass == arr:
        s = s + nbUnits*(time - t_old)
        nbUnits = nbUnits + 1
        t = time + expo(mtba)
        ev = cs.CREATE_EV(t,arr)
        EvL.InsertEv(ev)
        t_next_arr = t
    # ----------
    elif nclass == dep:
        s = s + nbUnits*(time - t_old)
        nbUnits = nbUnits - 1
        if nbUnits > 0:
            t = time + expo(mst)
        else:
            t = t_next_arr + expo(mst)
        ev = cs.CREATE_EV(t,dep)
        EvL.InsertEv(ev)
     # ----------
    elif nclass == cs.END_SIM:
        s = s + nbUnits*(T - t_old)
        meanNbOfUnits = s/T
     # ----------
    else:
        print("Error")
    #
    #
    t_old = time
    ### --- central simulation loop

# --- output    
print("\n --- meanNbOfUnits = %f\n" % meanNbOfUnits)

        
    