numeros = [2, 4, 1, 45, 75, 22]

print("ordenar los datos con sort.")
#ordena los datos 
numeros.sort()
print(numeros)
print("\n")

print("ordenando los datos al réves con reverse.")
#ordenando los datos al revés
numeros.sort(reverse=True)
print(numeros)

print("\n")
numeros_a = [2, 4, 1, 45, 75, 22]
print("Sorted: devuelve una nueva lista ordenada.")
numeros_2 = sorted(numeros_a)
print(numeros_a)
print(numeros_2)

print("\n")
print("ordenando los datos al réves con sorted con reverse.")
numeros_2 = sorted(numeros_a, reverse=True)
print(numeros_2)

print("\n")
print("ordenando listas dentro de otras listas con sort, como los números estan al inicio no hay problema de orden ")
usuarios = [[4, "Israel"], [1, "Felipe"], [5, "Pulga"]]
usuarios.sort()
print(usuarios)

print("\n")
print("ordenando los elmentos mediante un función.")
usuarios_a = [["Israel", 4], ["Felipe", 1], ["Pulga", 5]] 

def ordena(elemento):
    return elemento[1] # el 1 indica el elemento "4" de nuestra listap por lo cual ordena a partir de este, si lo cambiamos por 0 ordena apatir de "Israal"


#para ordenara la lista al réves usamos reverse
#usuarios.sortr(key=ordena, reverse=True)
usuarios_a.sort(key=ordena)
print(usuarios_a)