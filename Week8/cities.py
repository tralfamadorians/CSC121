def describe_city(city, country = 'iceland'): 
    # Prints which country the city is in
    print(f"{city.title()} is in {country.title()}.")

describe_city('reykjavik')

describe_city('vik')

describe_city(city = 'sevilla', country = 'spain')