#Ciclos, estructura de control
#Ciclo For
#Se usa cuando sabemos cuantas veces repetir un cierto grupo
#de instrucciones

#sintaxis
#for variable in range(inicio, fin, step):
    #codigo

#variable de control: se puede usar en el codigo que se repite
#range
for i in range(4):
    print(i)

for char in "Loops":
    print(char)

for num in [1,2,3]:
    print(num)

teams = {"a": "Red Bull", "b": "Mercedes", "c": "Ferrari"}
for clave in teams:
    print(clave)

for valor in teams.values():
    print(valor)
for clave,valor in teams.items():
    print(clave,valor)


#while<condicion>:
    #codigo
#no tiene un numero predeterminado de iteraciones
#no actualizan variable de control
     
x = 5
while x < 35:
    print(x)
    x += 5
