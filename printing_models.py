def print_models(unprinted_designs, completed_models):
   
    """
    Considera una compañia que hace impresiones 3D
    
    La primer función controla la impresión de los diseños y los 
    mueve a una lista llamada "completed_models"
    después de imprimirlo en pantalla.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")

def show_completed_models(completed_models):
    """La segunda función muestra todos los modelos que han sido impresos"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)