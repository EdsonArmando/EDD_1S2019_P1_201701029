import random

class Food:
    def __init__(self):
        self.x_coordinate = random.randint(0,60)
        self.y_coordinate = random.randint(0,20)
        type = random.randint(0,40)
        if type <=5 :
            self.type_food = 0 #0 == bad food (*)
        else:
            self.type_food = 1 #1 == good food (+)

    def print(self):
        print('x-coordinate: ', self.x_coordinate)
        print('y-coordinate: ', self.y_coordinate)
        if self.type_food==1:
            print('food: good')
        else:
            print('food: bad')


for x in range(0, 10):
    food = Food()
    food.print()
