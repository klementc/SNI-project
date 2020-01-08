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
from collections import deque

def expo(mean):
    return -mean*log(np.random.random_sample())

arr = 1		# event-class: arrivals
dep = 2		# event-class: departures

def sim_mminf(mtba,mst,T,seed,K):
    np.random.seed(seed)

    # --- first operations on the scheduler

    EvL = cs.LinkedList(T)	# --- end of simulation at time T

    t = expo(mtba)
    ev = cs.CREATE_EV(t,arr)
    EvL.InsertEv(ev)	# --- first arrival at time t

    s = 0.0
    nbUnits = 0
    t_old = 0.0
    nb_served = 0
    queue = deque([])
    totresponsetime = 0
    totjitter = 0
    oldjitter = -1

    nclass = -1
    # --- main loop
    while nclass != cs.END_SIM and nb_served != K:
        time, nclass = EvL.FirstEv()
        # ----------
        if nclass == arr:
            queue.append(time)
            s = s + nbUnits*(time - t_old)
            nbUnits = nbUnits + 1
            #
            t = time + expo(mtba)
            ev = cs.CREATE_EV(t,arr)
            EvL.InsertEv(ev)   # --- next arrival at time t
            #
            t = time + expo(mst)
            ev2 = cs.CREATE_EV(t,dep)
            EvL.InsertEv(ev2)   # --- next departure at time t
            # ----------
        elif nclass == dep:
            s = s + nbUnits*(time - t_old)
            nbUnits = nbUnits - 1
            #print("a:"+str(queue[0])+" d:"+str(time))
            rt = time - queue.popleft()
            totresponsetime += rt
            if(oldjitter != -1):
                totjitter += abs(rt-oldjitter)
            oldjitter = rt

            nb_served = nb_served + 1
            if(nb_served == K):
                meanNbOfUnits = s/time
            # ----------
        elif nclass == cs.END_SIM:
            s = s + nbUnits*(T - t_old)
            meanNbOfUnits = s/T
            # ----------
        else:
            print("Error")
            #
        t_old = time
    # --- end of main loop

    # --- ouput
    print("\n %d clients were served out of %d Maximum" % (nb_served, K))
    print("\n --- meanNbOfUnits = %f\n" % meanNbOfUnits)
    print("mean service time: "+str(totresponsetime/nb_served))
    print("mean service jitter: "+str(totjitter/(nb_served-1))) 


if __name__ == "__main__":
    params = sys.argv[1:]
    if len(params) != 5:
        print("\nUsage: %s  mtba  mst  T  seed K\n" % sys.argv[0])
        exit(0)
    else:
        mtba = float(sys.argv[1])	# mean time between arrivals
        mst = float(sys.argv[2])		# mean service time
        T = float(sys.argv[3])			# total simulation time
        seed = int(sys.argv[4])		# seed for the pseudo-random numbers
        K = int(sys.argv[5])
        print("\n --- Data: mtba = %.1f, mst = %.1f, T = %.1f, seed = %d" % (mtba,mst,T,seed))
        sim_mminf(mtba,mst,T,seed,K)



    
