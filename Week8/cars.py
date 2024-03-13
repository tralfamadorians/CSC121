def car(manufacturer, model, **car):
    # Car dictionary with make, model and any additional information
    car['make'] = manufacturer
    car['model'] = model
    return car

myCar = car('jeep', 'wrangler', color='black', year=1993)
print(myCar)
