#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import math
from numpy import *
import trajectory as tr

class Planet:
    def __init__(self, name, epsilon, period, a_axe):
        self.name = name
        self.epsilon = epsilon
        self.period = period
        self.a_axe = a_axe

    #Calcula la distancia del planeta al sol (módulo).
    def sunDistance(self,pos):
        return sqrt(pos[0]**2+pos[1]**2)

    def sunDistanceTime(self, time):
        gi = (2*math.pi)/self.period*(time)
        u = tr.besselFunctionMethod(self.epsilon, gi, 30, False)
        pos_x = self.a_axe*(cos(u)-self.epsilon)
        pos_y = self.a_axe*(sqrt(1-self.epsilon*self.epsilon)*sin(u))
        pos = [pos_x, pos_y]
        return sqrt(pos[0]**2+pos[1]**2)

    #Calcula la velocidad que lleva el planeta dependiendo de la anomalia excentrica y su derivada.
    def velocity(self, u, du):
        return [self.a_axe*(-sin(u))*du, self.a_axe*(sqrt(1-self.epsilon*self.epsilon)*cos(u)*du)]

    #Calcula el momento angular del planeta (constante)
    def angular_moment(self,time):
        gi = (2*math.pi)/self.period*(time)
        u = tr.besselFunctionMethod(self.epsilon, gi, 30, False)
        x = [self.a_axe*(cos(u)-self.epsilon),self.a_axe*(sqrt(1-self.epsilon*self.epsilon)*sin(u))]
        #Calculamos mu
        mu = ((2*math.pi)/self.period*sqrt(self.a_axe**3))**2
        #Calculamos la derivada de u
        du = (sqrt(mu)/sqrt(self.a_axe**3))*(1-self.epsilon*cos(u))
        dx = self.velocity(u, du)
        c = cross([x[0],x[1],0],[dx[0], dx[1], 0])
        return c

    #Calcula módulo del momento angular del planeta
    def module_angular_moment(self, time):
        c = self.angular_moment(time).tolist()
        return sqrt(c[0]**2+c[1]**2+c[2]**2)

    #Calcula el área recorrida del planeta entre dos instances
    def area(self, t_1, t_2):
        return 0.5*self.module_angular_moment(5)*(t_2-t_1)

    #Calcula la energía del planeta para un instante t dado (constante)
    def energy(self, time):
        #posición para u
        gi = (2*math.pi)/self.period*(time)
        u = tr.besselFunctionMethod(self.epsilon, gi, 30, False)
        pos = [self.a_axe*(cos(u)-self.epsilon),self.a_axe*(sqrt(1-self.epsilon*self.epsilon)*sin(u))]
        #Calculamos mu
        mu = ((2*math.pi)/self.period*sqrt(self.a_axe**3))**2
        #Calculamos la derivada de u
        du = (sqrt(mu)/sqrt(self.a_axe**3))*(1-self.epsilon*cos(u))
        #Calculamos la velocidad
        dx = self.velocity(u, du)
        #Calculamos la energia
        h = (self.sunDistance(dx)**2)/2-mu/self.sunDistance(pos)
        return h

    def getName(self):
        return self.name

    def getEpsilon(self):
        return self.epsilon

    def getPeriod(self):
        return self.period

    def getA_axe(self):
        return self.a_axe

    #Calcula la trayectoria del planeta usando el método de Newton-Raphson
    def trajectoryNR(self, nDivisions):
        times = []
        tray_x = []
        tray_y = []

        #Definición de las funciones
        keplerf = lambda u: u-self.epsilon*sin(u)
        dkeplerf = lambda u: 1-self.epsilon*cos(u)

        for i in range(nDivisions+1):
            times.insert(len(times), period*i/nDivisions)

        for t in times:
            gi = (2*math.pi)/self.period*(t)
            u = tr.NewtonsRaphsonMethod(keplerf, dkeplerf, math.pi, gi, 30, False)
            pos_x = self.a_axe*(cos(u)-self.epsilon)
            pos_y = self.a_axe*(sqrt(1-self.epsilon*self.epsilon)*sin(u))
            tray_x.insert(len(tray_x), pos_x)
            tray_y.insert(len(tray_y), pos_y)

        #print(str(tray_x))
        #print(str(tray_y))
        return [tray_x,tray_y]

    #Calcula la trayectoria del planeta usando la función de Bessel
    def trajectoryBessel(self, nDivisions):
        times = []
        tray_x = []
        tray_y = []

        #Definición de las funciones
        keplerf = lambda u: u-self.epsilon*sin(u)
        dkeplerf = lambda u: 1-self.epsilon*cos(u)

        for i in range(nDivisions+1):
            times.insert(len(times), self.period*i/nDivisions)

        for t in times:
            gi = (2*math.pi)/self.period*(t)
            u = tr.besselFunctionMethod(self.epsilon, gi, 30, False)
            pos_x = self.a_axe*(cos(u)-self.epsilon)
            pos_y = self.a_axe*(sqrt(1-self.epsilon*self.epsilon)*sin(u))
            tray_x.insert(len(tray_x), pos_x)
            tray_y.insert(len(tray_y), pos_y)

        #print(str(tray_x))
        #print(str(tray_y))
        return [tray_x,tray_y]


    #Obtiene la posición de un planeta para un punto dado usando Newton-Raphson.
    def positionNR(self, time):
        gi = (2*math.pi)/self.period*(time)
        keplerf = lambda u: u-self.epsilon*sin(u)
        dkeplerf = lambda u: 1-self.epsilon*cos(u)

        u = tr.NewtonsRaphsonMethod(keplerf, dkeplerf, math.pi, gi, 30, False)
        pos_x = self.a_axe*(cos(u)-self.epsilon)
        pos_y = self.a_axe*(sqrt(1-self.epsilon*self.epsilon)*sin(u))

        return [pos_x,pos_y]

    #Obtiene la posición de un planeta para un punto dado usando la función de Bessel.
    def positionBessel(self, time):
        gi = (2*math.pi)/self.period*(time)
        keplerf = lambda u: u-self.epsilon*sin(u)
        dkeplerf = lambda u: 1-self.epsilon*cos(u)

        u = tr.besselFunctionMethod(self.epsilon, gi, 30, False)
        pos_x = self.a_axe*(cos(u)-self.epsilon)
        pos_y = self.a_axe*(sqrt(1-self.epsilon*self.epsilon)*sin(u))

        return [pos_x,pos_y]
