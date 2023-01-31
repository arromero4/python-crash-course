def describe_mascota(nombreMascota, tipoAnimal = 'perrito'):

    """informacion de la mascota"""
    print(f"\nTengo un {tipoAnimal}.")
    print(f"Mi {tipoAnimal} se llama:  {nombreMascota.title()}.")

#Se puede excluir un argumento ya que está definido por default
describe_mascota(nombreMascota= 'harry')

