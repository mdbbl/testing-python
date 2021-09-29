cars=100
space_in_a_car = 4.0
passengers = 30
car_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity=cars_driver_space_in_a_car
#explain comments
average_passengers_per_car=passengers/cars_driven
print("there are",cars,"cars available")
print("there are only",drivers,"drivers available")
print("there will be",cars_not_driven,"emty cars today")
print("we can transport",carpool_capacity,"people today")
print("we have a",passenger,"carpool today")
print("we need to put about",average_passenger_per_car,"in each car")