# Unlimited number of tuple arguments
def add(*args):
    y = 0
    for n in args:
        y += n
    print(y)

add(3, 5, 6, 3, 23, 43, 45, 456)

# Unlimited number of keyword arguments
def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        # Using "get" prevents an error if during object initialisation a argument is not defined
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.year = kw.get("year")

my_car = Car(make="Subaru", model="Liberty")
print(my_car.model)
