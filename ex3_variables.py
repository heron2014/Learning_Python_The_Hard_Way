cars = 100 # cars is equal to 100 - we have 100 cars
space_in_car = 4.0 # space in a car is equal to 4, we have 4 seats in a car
drivers = 30 # We have 4 drivers
passangers = 90 # we have 90 passangers
cars_not_driven = cars - drivers # We have some cars that are not going to be used because not enough drivers
cars_driven = drivers # We have equal amount of cars as drivers
carpool_capacity = cars_driven * space_in_car # We have availble 120 seats availble 
average_passangers_per_car = passangers / cars_driven # Avarage passanger per car 

print 'There are', cars, 'cars available.'
print 'There are only', drivers, 'drivers available.'
print 'There will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capacity, 'poeple today.'
print 'We have ', passangers, 'passangers to carpool today.'
print 'We need to put about', average_passangers_per_car, 'in each car.' 
