# creating a class example

from typing import is_typeddict


class car():
    # attributes of a car
    wheels = 4
    doors = 2
    engine = True

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False
    
    # str dunder 
    def __str__(self):
        return f'{self.make} {self.model} {self.year}'
    
    def stop(self):
        if self.is_moving:
            print("the car has stopped")
            self.is_moving = False
        else:
            print('the car has already stopped')
    
    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('the car starts moving')
                self.is_moving = True
            print(f'the car is going {speed}')
        else:
            print("YOU HAVE RUN OUT OF GAS")
            self.stop()

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 50:
            return False
        else:
            return True



car_one = car("Ford", "Mustang", 2021)
car_two = car("BMW", "M4", 2018)
car_three = car("Ford", "Fiesta", 2000)
print(car_one.make)
print(car_two.make)

# change car_one year
car_one.year = 2020
print(car_one.year)

# make the car stop
car_one.stop()

# make the car go with speed
car_one.go('fast')

# testing if car is moving or stopped
car_one.stop()
car_one.stop()

# print dunder string
print(str(car_one))

