# class Base:
#     def m(self):
#         print("inside Base class")
#
# class Derived:
#     def m2(self):
#         print("inside derived")
#
# ob = Derived()
# ob.m2()

#single inheritance

class Base:
    def m(self):
        print("inside Base class")


class Derived(Base):
    def m2(self):
        print("inside derived")


ob = Derived()
ob.m2()
ob.m()

