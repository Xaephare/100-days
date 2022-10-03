def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(3, 5, 6, 7, 3))


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make='nissan')
print(my_car.model)
print(my_car.make)
