class Ten:
    def __get__(self, obj, objtype=None):
        print(self, obj, objtype)
        return 10

    def __call__(self):
        return f"{self} called"

import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute

