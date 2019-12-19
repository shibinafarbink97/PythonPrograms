# no1 = int(input("enter a num"))
# no2 = int(input("enter a num"))
# lst = [10,20,30]
# try:
#     res = no1/no2
#     print("res = ",res)
#     print(lst[5])
# except Exception as e:
#     print(e.args)
#
# print("i have one database connection")


no1 = int(input("enter a num"))
no2 = int(input("enter a num"))
lst = [10,20,30]
try:
    res = no1/no2
    print("res = ",res)
except Exception as v:
    print(v.args)
try:
    print(lst[5])
except Exception as e:
    print(e.args)
finally:
    print("database closed")