class Cat:
    def __int__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows")


class Lion(Cat):
    def __int__(self, name, pride_name):
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f"{self.name} roars")


class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs")




