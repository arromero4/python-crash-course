def car_info(manufacturer, model, **carData):
    """Información de auto"""
    carData['manufacturer'] = manufacturer
    carData['model'] = model
    return carData


car = car_info('subaru','outback', color='blue', tow_package=True)

print(car)