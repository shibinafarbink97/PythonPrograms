f1 = open("/home/luminar/PycharmProjects/luminarpython/file io/student",'r')
studset = set()        #create a null set
for item in f1:
    studset.add(item.rstrip("\n"))           #adding data from student to studset
print(studset)

f2 = open("/home/luminar/PycharmProjects/luminarpython/file io/failed",'r')
failset = set()
for item in f2:
    failset.add(item.rstrip("\n"))
print(failset)

passed=studset-failset
print(passed)

f3 = open("passed.txt",'w')
for item in passed:
    f3.write(item+"\n")