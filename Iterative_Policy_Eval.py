# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:45:37 2020

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt

from Gridworld import standard_grid

SMALL_ENOUGH = 10e-4

def print_values(V,g):
    for i in range(g.width):
        print("---------------------------")
        for j in range(g.height):
            v = V.get((i,j),0)
            if v>=0:
                print(" %.2f|" % v, end = "")
            else:
                print("%.2f|" % v, end = "")
        print("")

def print_policy(P,g):
    for i in range(g.width):
        print("---------------------------")
        for j in range(g.height):
            a = P.get((i,j),' ')
            print("  %s  |" % a, end="")
        print("")

if __name__ == '__main__':
    grid = standard_grid()
    states = grid.all_states()
    
    '''Uniform random policy'''
    V = {}
    for s in states:
        V[s] = 0
    gamma = 1.0
    while True:
        biggest_change = 0
        for s in states:
            old_v = V[s]
            if s in grid.actions:
                new_v = 0
                p_a = 1.0/len(grid.actions[s])
                for a in grid.actions[s]:
                    grid.set_state(s)
                    r = grid.move(a)
                    new_v+= p_a*(r + gamma*V[grid.current_state()])
                V[s] = new_v
                biggest_change = max(biggest_change,np.abs(old_v - V[s]))
        if biggest_change<SMALL_ENOUGH:
            break
    print("Values for uniformly random ction: ")
    print_values(V,grid)
    print("\n\n")
    
    '''Fixed Policy'''
    policy = {
    (2, 0): 'U',
    (1, 0): 'U',
    (0, 0): 'R',
    (0, 1): 'R',
    (0, 2): 'R',
    (1, 2): 'R',
    (2, 1): 'R',
    (2, 2): 'R',
    (2, 3): 'U'
    }
    print_policy(policy, grid)
    
    V = {}
    for s in states:
        V[s] = 0
    
    gamma = 0.9 
    
    while True:
        biggest_change = 0
        for s in states:
          old_v = V[s]
          if s in policy:
            a = policy[s]
            grid.set_state(s)
            r = grid.move(a)
            V[s] = r + gamma * V[grid.current_state()]
            biggest_change = max(biggest_change, np.abs(old_v - V[s]))
    
        if biggest_change < SMALL_ENOUGH:
          break
    print("values for fixed policy:")
    print_values(V, grid)
        
    
        
        