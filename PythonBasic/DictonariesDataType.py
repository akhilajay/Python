print('Dictonaries')
#key value pair
#similar to list, but cant join using "+"
##Map Declaration, with key:value
super_cars={'BMW': '$40K', 'Audi': '$41k', 'Benz': '$44k'}
print(super_cars)
#gettting value with key
print(super_cars['BMW'])
#delete
del super_cars['Benz']
print(super_cars)

#replace an item
super_cars['BMW']= '42K'
print(super_cars)

#lenght
print(len(super_cars))

#get by key
print(super_cars.get("Audi"))

#get all keys
print(super_cars.keys())

#get all values
print(super_cars.values())

#getting value from an idex
_list =list(super_cars.values())
print(_list[0])

