class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("inhale,exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.fins = "YES"

    def swim(self):
        print("swimming")

    def breathe(self):
        super(Fish, self).breathe()
        print("underwater")


animal = Animal()
print(animal.eyes)
animal.breathe()

print("\n")

nemo = Fish()
print(nemo.eyes)
nemo.swim()
print(nemo.fins)
nemo.breathe()

