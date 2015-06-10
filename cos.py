import math

x = input("Ingrese angulo: ")
n = input("Ingrese grado de precision: ")
cos=0
i=0

while (i < n):

    cos = cos + (pow(-1,i))*((pow(x,2*i))/(math.factorial(2*i)))
    i = i + 1

print("Valor aproximado: ")
print(cos)
print("Valor real: ")
print(math.cos(x))
    
