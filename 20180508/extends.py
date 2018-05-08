class BaseClassName:
    def parent_method(self):
        print("parent")


class DerivedClassName(BaseClassName):
    def chlid_method(self):
        BaseClassName.parent_method(self)
        self.parent_method()
        print("child")


c = DerivedClassName()

c.parent_method()
c.chlid_method()

print(isinstance(c, DerivedClassName))
print(isinstance(c, BaseClassName))
print(isinstance(c, int))
print(issubclass(DerivedClassName, BaseClassName))
print(issubclass(BaseClassName, DerivedClassName))
