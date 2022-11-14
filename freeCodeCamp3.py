#funcion
#bloque de codigo reutilizable que realiza una tarea especifica
#def <funcion> ():
    #codigo

def mostrar_mensaje():
    print("Hello world!")

mostrar_mensaje()

#parametro es una variable que es parte de la funcion
#y guarda un valor que podemos pasar cuando
#se llama a la funcion

#def <funcion> (<parametro>):
    #codigo
def mostrar_doble(num1, num2):
    
#proposito es que la funcion retorne un valor
    #return <valor>
    return num1 + num2

#argumento
#es un valor que se asing a un parametro cuando
#se llama a la función

resultado = mostrar_doble(1,2)
print(resultado)
#cuando se ejecuta return se detiene la funcion

#Scope, alcance de una variable en el programa
#determina a que variable se tiene acceso en el programa

#dos tipos:
#Global: definidas en el programa principal
#Local: definidas en una función

x = 5 #<== Variable global
def f(y) #<=== variable local porque está en la funcion
    print(x + y )
f(2)
