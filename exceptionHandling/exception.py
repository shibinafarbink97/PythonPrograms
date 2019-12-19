# no1 = int(input("enter a num"))
# no2 = int(input("enter a num"))
# try:
#     res = no1/no2
#     print("res = ",res)
# except:
#     print("exception occured")
# print("i have one database connection")


no1 = int(input("enter a num"))
no2 = int(input("enter a num"))
try:
    res = no1/no2
    print("res = ",res)
except:
    no2 = int(input("enter a num"))
    try:
        res = no1/no2
        print("res = ",res)
    except:
        print("exception occured")
print("i have one database connection")