#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from trajectory import *
from planet import *
from anima import *

# Lista de planetas que se usarán para la representación:
planets = []

# Función que permite la entrada por consola de una
# función u(t) para la anomalía excéntrica
def inputFormulaConsole():
    variable = "t"
    formula = raw_input("Ingresa la funcion u(t) para la anomalia excentrica: ")
    expr = "lambda " + variable + ": " + formula
    return eval(expr)

# Función para dibujar una función en un intervalo
def genericPlot(formula, init, end):
    x = linspace(init,end,500)
    plt.plot(x,formula(x))
    plt.show()

# Función que sirve para generar un menu para el usuario al seleccionar una
# opción para un planeta:
def planetSelector(planets):
    i=0;
    for planet in planets:
        print planet.getName() + "[" + str(i) + "]"
        i = i+1
    usage = int(raw_input("Introduce una opción: "))
    while usage >= len(planets) or usage < 0:
        print "Opción no permitida"
        i=0
        for planet in planets:
            print planet.getName() + "[" + str(i) + "]"
            i = i+1
        usage = int(raw_input("Introduce otra opción: "))
    return usage

# Obtiene las trayectorias de un archivo data con todos los planetas. Además
# es la función que se encarga de mostrar un menu selector para el usuario
# dandole la posibilidad de crear la representación de las trayectorias y de
# crear una animación con las mismas.
def calculateTrajectories(trajectory):

    os.system("clear")

    with open('./data.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            planet = Planet(row[0],float(row[2]), float(row[3]), float(row[1]), float(row[4]), float(row[5]), float(row[6]))
            planets.insert(len(planets), planet)

        usage = -1

        while usage != 5:

            print "Información Básica: "

            for planet in planets:
                print planet.getName()
                print "Energía : "+ str(planet.energy(80))
                print "Distancia al sol en el instante 0: " +str(planet.sunDistance(planet.positionBessel(0)))

            print "\nMenu:"
            print "Calcular las trayectorias de los planetas en 2D [0]"
            print "Calcular las trayectorias de los planetas en 3D [4]"
            print "Calcular las trayectorias de los planetas en 2D con animación [1]"
            print "Comparativa Bessel/Newton-Raphson [2]"
            print "Opciones para planetas [3]"
            print "Salir [5]"
            usage = int(raw_input("Introduce una opción: "))

            os.system("clear")

            if usage == 0:
                figure = plt.figure("tray")
                for planet in planets:
                    if trajectory == "NR":
                        tr = planet.trajectoryNR(100)
                    else:
                        tr = planet.trajectoryBessel(100)
                    plt.plot(tr[0],tr[1], label=planet.getName())
                plt.legend()
                #plt.show()
                plt.savefig("2d.png")
                plt.close()
            elif usage == 1:
                generateAnimation(planets)
            elif usage == 2:
                for i in range(30):
                    print "Posición Bessel = "+str(planets[2].positionBessel(i))+" / Posición Raphson: "+str(planets[2].positionNR(i))
                raw_input("Pulsa cualquier botón para continuar...")
                os.system("clear")
            elif usage == 3:
                print "Opciones de planetas:"
                print "Calcular posicion es un instante [0]"
                print "Calcular momento angular [1]"
                print "Calcular energía [2]"
                print "Calcular área entre dos instantes [3]"
                print "Calcular la distancia al sol [4]"
                print "Calcular la posición en R3 [5]"
                print "Atras [6]"
                opt = int(raw_input("Introduce una opción: "))

                os.system("clear")

                if opt == 0:
                    optp = planetSelector(planets)
                    time = float(raw_input("Introduce un instante:"))
                    pos = planets[optp].positionBessel(time)
                    pos2 = planets[optp].positionNR(time)
                    print "La posición en el instante " + str(time)+ " para el planeta " + planets[optp].getName() + "usando NR es " + str(pos2)
                    print "La posición en el instante " + str(time)+ " para el planeta " + planets[optp].getName() + "usando Bessel es " + str(pos)
                elif opt == 1:
                    optp = planetSelector(planets)
                    time = float(raw_input("Introduce un instante:"))
                    c = planets[optp].angular_moment(time)
                    print "el momento angular en el instante " + str(time) + " para el planeta " + planets[optp].getName() + " es " + str(c)
                elif opt == 2:
                    optp = planetSelector(planets)
                    time = float(raw_input("Introduce un instante:"))
                    h = planets[optp].energy(time)
                    print "La energía en el instante " + str(time) + " para el planeta " + planets[optp].getName() + " es " + str(h)
                elif opt == 3:
                    optp = planetSelector(planets)
                    time_1 = float(raw_input("Introduce el primer instante:"))
                    time_2 = float(raw_input("Introduce el primer instante:"))
                    A = planets[optp].area(time_1, time_2)
                    print "El área barrida entre los instantes para el planeta " + planets[optp].getName() + " es " + str(A)
                elif opt == 4:
                    optp = planetSelector(planets)
                    time = float(raw_input("Introduce un instante:"))
                    d = planets[optp].sunDistanceTime(time)
                    print "La distancia en el instante " + str(time) + " para el planeta " + planets[optp].getName()+  " es " + str(d)
                elif opt == 5:
                    optp = planetSelector(planets)
                    time = float(raw_input("Introduce un instante:"))
                    pos = planets[optp].position3D
                    print "La posición en el instante " + str(time)+ " para el planeta " + planets[optp].getName() + "usando Bessel es " + str(pos)

                raw_input("Pulsa cualquier botón para continuar...")
                os.system("clear")
            elif usage == 4:
                fig = plt.figure()
                ax = plt.axes(projection='3d')
                for i in ["x","y","z"]:
                    patch = plt.Circle((0, 0), 0.1, fc='y')
                    ax.add_patch(patch)
                    art3d.pathpatch_2d_to_3d(patch, z=0, zdir="i")
                for i in range(len(planets)-4):
                    tr = planets[i].trajectory3D(4)
                    ax.plot(tr[0], tr[1], tr[2])
                plt.savefig("3d_1.png")
                plt.close()

                fig = plt.figure()
                ax = plt.axes(projection='3d')
                for i in ["x","y","z"]:
                    patch = plt.Circle((0, 0), 0.1, fc='y')
                    ax.add_patch(patch)
                    art3d.pathpatch_2d_to_3d(patch, z=0, zdir="i")
                for i in range(len(planets)):
                    tr = planets[i].trajectory3D(4)
                    ax.plot(tr[0], tr[1], tr[2])
                plt.savefig("3d_2.png")
                plt.close()
                raw_input("Pulsa cualquier botón para continuar...")
                os.system("clear")

            elif usage == 5:
                print "Finalizando..."
                print "Finalizado"
            else:
                print "Opción no permitida."
                raw_input("Pulsa cualquier botón para continuar...")
                os.system("clear")

# Cuerpo principal del programa, tan solo se eleige con que calcular las
# trayectorias y ejecuta el método anterior.
if __name__ == "__main__":
    usage = raw_input("Calcular la trayectorias usando la función de Bessel o Newton-Raphson (B/NR - B default): ")
    calculateTrajectories(usage)
