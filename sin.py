#!/usr/bin/python
import math,sys

#x = input("Ingrese angulo: ")
#n = input("Ingrese grado de precision: ")

sin=0
angle_rad = 0
if(len(sys.argv)==1):
    print("Usage: sin.py -c [angle] [precision]")
    sys.exit(0)
if sys.argv[1]=="-c" and len(sys.argv)==4:
    i=0
    factor=0.0174532925
    rad = float(sys.argv[2])*factor
    angle_rad=rad
    while (i < int(sys.argv[3])):
        sin = sin + ((pow(-1,i))*((pow(rad,2*(i)+1))/(math.factorial(2*i+1))))
        i = i + 1
else:
    print("Wrong argument or usage")
    sys.exit(0)
##print(str(sys.argv))
print("Valor aproximado: ")
print(sin)
print("Valor real: ")
print(math.sin(angle_rad))
    
