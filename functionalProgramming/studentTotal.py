class Student:
    def __init__(self,id,name,total):
        self.id =id
        self.name=name
        self.total=total
    def __str__(self):
        return self.name


f1 = open("/home/luminar/PycharmProjects/luminarpython/functionalProgramming/student",'r')
lst = []
studentList = []
for data in f1:
    lst = (data.rstrip("\n").split(","))
    print(lst)
    id = lst[0]
    name = lst[1]
    total = lst[2]
    studentList.append(Student(id,name,total))


mlist = list(filter(lambda o:int(o.total)>150,studentList))
for ob in mlist:
    print(ob)



