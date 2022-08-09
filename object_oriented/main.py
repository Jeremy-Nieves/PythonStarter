class Dog:

    species = 'C. Lupus'
    num_dogs = 0

    @classmethod
    def register_stray(cls):
        return cls('coming soon', 'unknown', 'unknown')

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.trick = []
        Dog.num_dogs += 1

    def bark(self):
        print(f"{self.name} says WOOF!")

    def learn_trick(self, new_trick):
        if new_trick not in self.trick:
            self.trick.append(new_trick)

    def perform_trick(self, trick):
        if trick in self.trick:
            print(f"{self.name} performs {trick}!")
        else:
            print(f"{self.name} doesn't know {trick}")

lando = Dog('Lando', 'australian shep', 'NJ')
pension = Dog('Penny', 'doxen', 'myheart')

pension.learn_trick('be cute')
pension.learn_trick('beg')
pension.learn_trick('cry')
lando.learn_trick('sit')
lando.learn_trick('down')
lando.learn_trick('stay')
lando.learn_trick('hump')
lando.perform_trick('stay')
Dog.register_stray()

pension.bark()
print(lando.trick)
print(pension.trick)
print(lando.breed)
print(pension.species)



