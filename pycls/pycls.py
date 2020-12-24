class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

mc = MyClass()
print(mc.method())
print(MyClass.staticmethod())
print(MyClass.classmethod())

f = MyClass.classmethod
print(f())