def describe_city(city, country = 'iceland'): 
    print(f"{city.title()} is in {country.title()}.")

describe_city('reykjavik')

describe_city('vik')

describe_city(city = 'sevilla', country = 'spain')