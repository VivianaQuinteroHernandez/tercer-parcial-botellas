# 	* Universidad Sergio Arboleda
#	* Fecha: 25 de mayo de 2022
#	* Autora: Ángela Viviana Quintero Hernández
#	* Materia: Parallel Computing
#	*Tema: Implemantación para el archivo mandel en Cython

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(ext_modules=cythonize("heat_cyt.pyx"), include_dirs=[numpy.get_include()])
