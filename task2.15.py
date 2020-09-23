name = {'Усейн Болт': '1', 'Umut': '2', 'Aibek': '3'}
place = {'1': 'UB', '2': 'Umut', '3': 'Aibek'}
def get_key(value):
    print(name[value])
def get_value(key):
    print(place[key])

get_key(input('Name: '))

get_value(input('Place: '))