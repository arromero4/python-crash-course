def get_formatted_citi(city, country, population=''):
    """parameters optional"""
    if population:
        full_info = f"{city}, {country} - Population {population}"
    else:
        full_info = f"{city}, {country}"
    return full_info.title()
