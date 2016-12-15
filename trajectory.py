#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import scipy.special as sp
#from mpl_toolkits.mplot3d import Axes3D
from numpy import *
from planet import *

# Función que implementa el método de Newton-Raphson
def NewtonsRaphsonMethod(function, derivate, init_u, gi, N, trace):
    error = 0.0000001
    if 0 <= gi and gi <= 2*math.pi+error:
        if 0 <= init_u and init_u <= math.pi:
            u = []
            u.insert(len(u), init_u)
            for i in range(N):
                u.insert(len(u), u[i]-(function(u[i])-gi)/derivate(u[i]))
                if trace:
                    print("u[" + str(i) + "]: " + str(u[i]))
            return u[len(u)-1]
        else:
            print("El valor de inicio no está entre 0 y pi.")
    else:
        print("El valor de gi no está entre 0 y 2pi.")
    return -1

def besselFunctionMethod(epsilon, gi, N, trace):
    besselSum = 0
    for n in range(1,N+1):
        besselSum = 2/n*sp.jv(N,n*epsilon)*sin(n*gi)
    if trace:
        print(besselSum+gi)
    return gi+besselSum
