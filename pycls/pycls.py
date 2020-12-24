class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

    def mymethod():
        return "mymethod"

mc = MyClass()
print(mc.method())
print(mc.staticmethod())
print(MyClass.staticmethod())
print(MyClass.classmethod())

f = MyClass.classmethod
print(f())
print(MyClass.method(mc))
try:
    print(MyClass().mymethod())
except Exception as e:
    print("Exception raised:", e)

print(MyClass.method("BOOOO"))
