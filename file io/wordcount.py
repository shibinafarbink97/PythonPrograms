import operator
f1 = open("/home/luminar/PycharmProjects/luminarpython/file io/words",'r')
lst =[]
dict = {}
for data in f1:
    lst = (data.rstrip("\n").split(" "))

    for word in lst:
      if(word not in dict):
        dict[word]=1
      else:
        dict[word]+=1
print(dict)

sorted_dict= sorted(dict.items(), key=operator.itemgetter(1))
print(sorted_dict[-1])