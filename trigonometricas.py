#!/usr/bin/python
# -*- coding: utf-8 -*-
import math,sys

class trigonometricas:

	def __init__(self):
		x = raw_input("Hola, que operación desea efectuar. \nPara seno ingrese 1,Para coseno ingrese 2\nRespuesta: ")
		if x == "1":
			#print("seno")
			self.sin()
		elif x == "2":
			#print("coseno")
			self.cos()
		else:
			print("Respuesta erronea")
			sys.exit(0);

	def sin(self):
		x = raw_input("Ingrese angulo: \n")
		y = raw_input("Ingrese precision: ")
		factor=0.0174532925
		rad = int(x)*factor
		res = 0
		i = 0
		xx = int(y)
		sin = 0
		while (i < xx):
			sin = sin + ((pow(-1,i))*((pow(rad,2*(i)+1))/(math.factorial(2*i+1))))
			i = i + 1
		print(sin)
		return

	def cos(self):
		x = raw_input("Ingrese angulo: \n")
		y = raw_input("Ingrese precision: ")
		factor=0.0174532925
		rad = int(x)*factor
		res = 0
		i = 0
		xx = int(y)
		cos = 0
		while (i < xx):
			cos = cos + (pow(-1,i))*((pow(rad,2*i))/(math.factorial(2*i)))
			i = i + 1
		print(cos)
		return

inicio = trigonometricas()
		