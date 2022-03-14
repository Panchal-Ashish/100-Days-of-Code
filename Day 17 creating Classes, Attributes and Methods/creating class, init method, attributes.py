# constructor  # init method
# attribute is a variable assigned to an object (may or may not within the class)
# attribute is a thing that a object has
# method are the things that the object does
# init method is initialized(triggered) everytime a new object is called from the class


class User:
    def __init__(self):
        print("new user being called...")


user1 = User()
user1.id = "001"   #id is an sttribute to object user 1
user1.name = "Ash"
print(user1.id)     # 001

user2 = User()
user2.id = "002"   #id is an sttribute to object user 2
user2.player = "002"   
print(user2.id)     # 002

# but if we have many objects, then it is not possible to give attributes to each of them separately..... this is error prone

# to avoid this,we use init method where we assign the attributes while calling the object (or class)
# In Init function, in addition the self, we can add as many paramerters as we want


class Car:
    def __init__(self,seats):
        self.seats = seats


c1 = Car(5)     # automatically assigns to seats
c1.wheels = 4   # not automatically assigned, but additional attribute created
print(c1.seats)     # 5
print(c1.wheels)    # 4



class User:
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username

user1 = User('001','ashish')
print(user1.user_id)
print(user1.username)
