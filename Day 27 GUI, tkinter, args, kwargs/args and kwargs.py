## ARGS ##  ... unlimited positional arguments... and stores in form of tuple

def add(*args):     # takes inputs and saves them as a tuple
    print(args[1])       # indexing
    sum = 0
    for arg in args:
        sum += arg
    #sum = args.sum()       # shows error bcoz tuple object has no attribute or method called sum()
    return sum

print(add(5,20,1563,156))



## KWARGS ## ... unlimited keyword arguments... stores in form of dictionary

# Example 1
def calculate(n, **kwargs):    # takes in inputs and saves as a dictionary... key = keyword, value = argument provided
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]      # indexing similar to dict... call by key, returns value
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5, divide= 1)      # divide is additional, but does not show error
## Note.. additional arguments passed are OK and do not show error
##       but insufficient arguments (less than mandatory ones) are NOT OK and shows error
##       this issue is sorted in 2nd example by using  kw.get() method


## Example 2
class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        ## can call without using "get" method, but it will show err if 'make' is not specified while calling the function
        self.model = kw.get("model")
        ## by using get method, if we dont specify the model, it is ok, no errs
        self.year = kw.get("year")

my_car = Car(make= "Hyundai", model= "Alcazar",year= 2021)
print(my_car.make, my_car.model)
