#Designar el arreglo
print("Definiendo el arreglo")
n = int(input("Defina el número de términos del arreglo: "))
D = []
i = 0
while i < n:
    t = int(input("Ingrese un número: "))
    D.append(t)
    i = i + 1 

#Mostrar el arreglo
print("El arreglo creado es", D)
print("Ahora pasará a ordenarse de forma ascendente")
print("...")

#Ordenar
ND = []
for u in range(len(D)):
    minim = D[0]
    for e in range(len(D)):
        if D[e] < minim:
            D[e] = minim
    D.remove(minim)
    ND.append(minim)

print(ND)



    


