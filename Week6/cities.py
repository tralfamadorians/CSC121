cities = {
    
    'asheville' : {
        'country' : 'united states',
        'population' : '94,067',
        'nickname' : 'land of the sky'
    },

    'barcelona' : {
        'country' : 'spain',
        'population' : '1.62 million',
        'nickname' : 'barna'
    },

    'paris' : {
        'country' : 'france',
        'population' : '2.161 million',
        'nickname' : 'the city of lights'
    }
}

for city,info in cities.items():
    print(f"Name: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population'].title()}")
    print(f"City Nickname: {info['nickname'].title()}\n")
