def build_person(first_name, last_name):
    """Regresa la info de una persona en un diccionario"""
    
    person = {'first': first_name, 'last': last_name}
    
    return person
musician = build_person('jimi', 'hendrix')
print(musician)