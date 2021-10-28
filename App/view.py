"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar analizador")
    print("2- Cargar información en el catálogo")
    print("3- Avistamientos por ciudad")
    print("4- Avistamientos por duración")
    print("5- Avistamientos en hora determinada")
    print("6- Avistamientos en cierta fecha")
    print("7- Avistamientos según la zona")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando..... :3")
        cont = controller.init()

    elif int(inputs[0]) == 2:
         print("Cargando información de los archivos ....")

    elif int(inputs[0]) ==3: 
        ciudad = input("Avistamiento de OVNI en la ciudad: ")
        cantidad = controller.getSizeCiudades(cont)
        resultado = controller.getAvisCiudad(ciudad, cont)
        top = controller.getTopCiudades() 
        print("\nHay un total de " + str(cantidad) + "diferentes ciudades con avistamientos ")
        print("El top 5 de ciudades  con mayores avsitamientos son: ")


    else:
        sys.exit(0)
sys.exit(0)
