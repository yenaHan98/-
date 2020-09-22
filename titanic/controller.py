from titanic.entity import Entity
from titanic.service import Service

class Controller:
    def  __init__(self):
        self.entity = Entity()
        self.service = Service()

    def preprocessing(self) -> object:
        pass

    def modeling(self) -> object:
        pass

    def learning(self):
        pass

    def submit(self):
        pass
    