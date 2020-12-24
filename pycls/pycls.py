class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

    @staticmethod
    def fun():
        pass

mc = MyClass()
print(mc.method())
print(mc.staticmethod())
print(MyClass.staticmethod())
print(MyClass.classmethod())

f = MyClass.classmethod
print(f())
print(MyClass.method(mc))
#print(MyClass().plain_method())
print(MyClass.method("BOOOO"))
