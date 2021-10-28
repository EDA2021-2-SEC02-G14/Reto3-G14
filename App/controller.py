"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    analyzer = model.newCatalog()
    return analyzer

# Funciones para la carga de datos

def loadData(analyzer, UFOfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    ufofile = cf.data_dir + UFOfile
    input_file = csv.DictReader(open(ufofile, encoding="utf-8"),
                                delimiter=",")
    for ufo in input_file:
        model.addCrime(analyzer, ufo)
    return analyzer

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

<<<<<<< HEAD
def UFOSize(analyzer):
    """
    Numero de UFO's leidos
    """
    return model.crimesSize(analyzer)
=======
def getSizeCiudades(catalog):
    """
    Numero de ciudades leidas
    """
    return model.ciudadesSize(catalog)
>>>>>>> a244b7296989e9d006b64badb94f129bf28a87ef
