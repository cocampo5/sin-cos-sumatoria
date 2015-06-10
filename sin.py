import math

x = input("Ingrese angulo: ")
n = input("Ingrese grado de precision: ")
sin=0
i=0

while (i < n):

    sin = sin + ((pow(-1,i))*((pow(x,2*(i)+1))/(math.factorial(2*i+1))))
    i = i + 1

print("Valor aproximado: ")
print(sin)
print("Valor real: ")
print(math.sin(x))
    
