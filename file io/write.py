# f = open("/home/luminar/PycharmProjects/luminarpython/file io/test")
# print(f.mode)



# lst =["abc","def","hij"]
# f = open("text.txt",'w')
# for item in lst:
#     f.write(item)

lst =["abc","def","hij"]
f = open("text.txt",'w')//write data
for item in lst:
    f.write(item+"\n")


lst =["abc","def","hij"]
f = open("text.txt",'a') //append data
for item in lst:
    f.write(item+"\n")