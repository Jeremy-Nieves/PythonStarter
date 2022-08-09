class Cat:
    def __int__(self, name):
        self.name = name

class Lion(Cat):

    def __init__(self, name, pride_name):
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f'{self.name} roars!!')

