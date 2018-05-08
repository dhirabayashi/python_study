class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = [1, 2, 3]

    def f(self):
        return 'hello world ' + str(self.data)


print(MyClass.i)
x = MyClass()

print(x.f())
print(x.f)
print(MyClass.f)
print(x.i)
print(x.__doc__)
print(x.data)

print(MyClass.f(x))

xf = x.f
print('****************')
print(xf())
