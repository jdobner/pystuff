from decorators.decorators import debug
import os, logging, logboot

class Ten:
    @debug
    def __get__(self, obj, objtype=None):
        return 10

    def __call__(self):
        return f"{self} called"


class DirectorySize:
    @debug
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute


@debug
class LoggedAccess:

    @debug
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', self.public_name, value)
        setattr(obj, self.private_name, value)


class Person:

    name = LoggedAccess()                # First descriptor instance
    age = LoggedAccess()                 # Second descriptor instance

    def __init__(self, name, age):
        self.name = name                 # Calls the first descriptor
        self.age = age                   # Calls the second descriptor

    def birthday(self):
        self.age += 1

