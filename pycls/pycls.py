import math
import requests


class MyClass:
    count = 0

    def __init__(self) -> None:
        type(self).count += 1
        self.id = self.count

    def method(self):
        return 'instance method called', self, self.id

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def mystaticmethod():
        return 'static method called'

    @staticmethod
    def staticmethod():
        return 'static method called'

    def mymethod():
        return "mymethod"

    def __set_name__(self, owner, name):
        pass


mc = MyClass()
print(mc.method())
print(mc.mystaticmethod())
print(MyClass.mystaticmethod())
print(MyClass.classmethod())

f = MyClass.classmethod
print(f())
print(MyClass.method(mc))
try:
    print(MyClass().mymethod())
except Exception as e:
    print("Exception raised:", e)
try:
    print(MyClass.method("BOOOO"))
except AttributeError as e:
    print(e)


class Pizza:
    def __init__(self, radius: int, *ingredients):
        self.radius = radius
        if len(ingredients) < 2:
            raise ValueError(f"{type(self)} must contain at least 2 ingredients")
        self.ingredients = list(ingredients)

    def __repr__(self):
        return f'{self.radius}" Pizza({self.ingredients!r})'

    @property
    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

    @classmethod
    def margherita(cls, radius):
        return cls(radius, 'mozzarella', 'tomatoes')

    @classmethod
    def prosciutto(cls, radius):
        return cls(radius, 'mozzarella', 'tomatoes', 'ham')


print(Pizza("hi", "ho", "there"))



class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
