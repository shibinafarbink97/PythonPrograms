class Parent:
    def property(self):
        print("100k gold 2car 10lakhs")
    def marraige(self):
        print("marraige with ajay")

class Child(Parent):
    def marraige(self):
        print("marraige with akhil")

ob=Child()
ob.property()
ob.marraige()