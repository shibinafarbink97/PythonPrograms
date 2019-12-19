num1=int(input("enter value"))
num2=int(input("enter value"))
num3=int(input("enter value"))
# if(num1<num2):
#     print("num2 greater")
# elif(num1>num2):
#     print("num1 greater")
# else:
#     print("equal")

# if(num1<0):
#     print("negative")
# elif(num1>0):
#     print("positive")
# elif(num1==0):
#     print("0")
# else:
#     print("invalid")

if(num1>=num2) and  (num1>=num3):
    print("num1 is greater")
elif(num2>=num1) and (num2>=num3):
    print("num2 is greater")
elif(num3>=num1) and (num3>=num2):
    print("num3 is greater")
elif(num1==num2==num3):
    print("equal")
else:
    print("null");
