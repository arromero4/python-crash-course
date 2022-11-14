#List
elem = [1,2,3,4,5]

print(elem.index(2))

#Cambiar elemento de lista
elem[0] = 6
print(elem)

#Metodos de las listas
#lista.metodo(parametros)
#count(elem)
#extend(list)
#pop()
#reverse()
#sort()
#sorted()

#Tupla (estructura inmutable)
items = (1,2,3,4,5)
print(1 in items)
#tupla.index(elem)
#tupla.count(elem) para contar ocurrencias


#diccionarios

dicc = {"Equipo": "RedBull", "Piloto": 11, "Compañero": "Max"}
print(dicc["Equipo"])
print(dicc["Piloto"])

#modificar diccionario
#diccionario[clave] = nuevo_valor
dicc["Piloto"] = "Checo"
print(dicc)

#Remover de diccionario
#del dicc[clave]
del dicc["Compañero"]
print(dicc)

#buscar en diccionario
print("Equipo" in dicc)
