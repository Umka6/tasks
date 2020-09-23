#_предупреждение
#__ = безопасное сокрытиcе данных

old_list = ['1','2','3','4','5','6','7']
new_list = []
for item in old_list:
    new_list.append(int(item))
print(new_list)

def miles_to_kilometers(num_miles):
    return num_miles * 1.6
mile_distances = [1.0,6.5,5.4,2.4,9]
kilometer_distances = list(map(miles_to_kilometers,mile_distances))
print(kilometer_distances)