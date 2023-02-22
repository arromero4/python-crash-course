"""ejemplo con diccionarios"""
cities = {
    'CDMX' : {
      'country': 'Mexico',
      'population': '8.8M',
      'fact': 'Capital of the country'
    },

    'Brasilia': {
      'country': 'Brasil',
      'population': '4.7M',
      'fact': 'Capital of the samba'
      
    },

    'Roma': {
      'country': 'Italy',
      'population': '10M',
      'fact': 'Capital of the Romance and The Colosseum'
      
    }
}


for city, info in cities.items():
    print(f"{city}: ")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")

