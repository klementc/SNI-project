#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --- pico-sim, ver 2019-v1

END_SIM = 0

class Event:
    def __init__(self,t,c):
        self.Time = t
        self.Class = c
        self.Next = None

def CREATE_EV(t,c):
    ev = Event(t,c)
    return ev

class LinkedList:
    def __init__(self, T):
        self.First = None
        self.InitEvList(T)
    
    # --- initializing the event-list (or "scheduler")
    def InitEvList(self, t):
        self.First = Event(t,END_SIM)
        
    # --- accessing and removing the first event
    def FirstEv(self):
        x = self.First
        self.First = self.First.Next
        t = x.Time
        c = x.Class
        x = None
        return t, c   
    
    # --- event insertion maintaining order
    def InsertEv(self, ev):
        x = None
        y = None
        time = ev.Time
        if time < self.First.Time:
            # --- ev will become the first one
            ev.Next = self.First
            self.First = ev
            return
        # --- here, ev goes at least at 2nd position 
        x = self.First
        y = x.Next
        while y != None:
            if time < y.Time:
                # --- ev goes after x end before y
                ev.Next = y
                x.Next = ev
                return
            x = y
            y = y.Next
        # --- ev goes after the whole list
        x.Next = ev
        ev.Next = None
        return
