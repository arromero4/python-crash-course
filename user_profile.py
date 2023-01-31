def perfil_usuario(nombre, apellido, **user_info):
    """Información de perfil"""
    user_info['nombre'] = nombre
    user_info['apellido'] = apellido
    return user_info
    
    
perfil_masculino = perfil_usuario('Andres', 'Romero', location='CDMX',
field='Software Engineering')

perfil_femenino = perfil_usuario('Melissa', 'Fararoni', location = 'Acayucan', field = 'Nursing')

print(perfil_masculino)
print(perfil_femenino)