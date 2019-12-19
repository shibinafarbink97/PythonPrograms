f1 = open("/home/luminar/Downloads/fakefriends.csv",'r')
dict = {}
for data in f1:
    data = data.rstrip()
    lst = data.split(",")
    age = lst[2]
    print("age",age)



    if(age not in dict):
        dict[age]=1
    else:
        dict[age]+=1
print(dict)