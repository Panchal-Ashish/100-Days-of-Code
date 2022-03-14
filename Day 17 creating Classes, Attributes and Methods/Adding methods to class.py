# attribute is a thing that a object has
# method are the things that the object does

class Car:
    def __init__(self,seats):
        self.seats = seats

    def enter_race_mode(self,wheels):      # adding methods
        self.seats = 2
        self.wheels = wheels

c1 = Car(5)
print(f"seats: {c1.seats}")
print(c1.wheels)    # this line produces err as wheels are not yet defined... or the methhod to set wheels id not called

c1.enter_race_mode(4)
print(f" seats after entering race mode: {c1.seats}")
print(f" wheels after entering race mode: {c1.wheels}")