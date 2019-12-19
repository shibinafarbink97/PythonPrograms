lst = [1,2,3,4,5,6,7,8]
lst = list(map(lambda no:no*no,filter(lambda no:no%2==0,lst)))  #here inner bracket work first ie,even number work first then square
print(lst)

