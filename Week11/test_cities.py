from city_country import get_location

#def test_get_location():
    #'''Does Santiago, Chile work?'''
    #location = get_location('santiago', 'chile')
    #assert location == 'Santiago, Chile'

def test_city_country_population():
    '''Does Santiago, Chile - population 500000 work?'''
    location = get_location('santiago', 'chile', 5000000)
    assert location == 'Santiago, Chile - Population 5000000'