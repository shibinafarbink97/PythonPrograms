class Student:
    clgname="luminar"

    def __init__(self,stname,id): #__init__  is constructor,initialise instance variable
        self.st_name=stname
        self.id=id
    def printVal(self):
        print("name=",self.st_name)
        print("id= ",self.id)


st=Student("ajay",1)
st.printVal()
