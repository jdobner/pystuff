#from https://realpython.com/primer-on-python-decorators/#first-class-objects


def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")



def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

def parent2(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


print(greet_bob(say_hello))
print(greet_bob(be_awesome))
print()
parent()
print()
first = parent2(1)
second = parent2(2)
print(first)
print(first())
print(second)
print(second())




def my_decorator(func):
    def wrapper():
        print(f"Something is happening before {func} is called.")
        func()
        print(f"Something is happening after {func} is called.")
    return wrapper

def say_whee():
    print("Whee!")

print()
say_whee = my_decorator(say_whee)
say_whee()

@my_decorator
def say_whee_deco():
    print("Whee are decorated!")

print()
say_whee_deco()

print()

from decorators import repeat, timer, debug

@repeat(num_times=2)
def say_whee2():
    print("Whee2!")

say_whee2()


@repeat(num_times=3)
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")

print()
greet(name="Jerry")
greet("Joe", "Bye")
greet(*['John', 'Shalom'])
greet("Josh", greeting="Halloooo")
print()


@repeat
@debug
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

print(return_greeting("JR"))
print()


@debug
@timer
def waste_some_time(num_times):
    return sum([i**2 for i in range(num_times)])

waste_some_time(1_000_000)


