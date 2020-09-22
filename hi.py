class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods = []

    def open(self):
        self.isOpened = True
        print('냉장고 문 옵 흔')

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 속에 음식이 들어감')
        else:
            print('냉장고 문이 닫혀있어서 못넣음..')

    def close(self):
        self.isOpened = False
        print('닫 어')

class Food:
    pass