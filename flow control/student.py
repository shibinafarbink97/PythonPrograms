m1 = int(input("enter mark"))
m2 = int(input("enter mark"))
m3 = int(input("enter mark"))
sum=(m1+m2+m3)
print("sum = ",sum)
if(sum>140):
 print("grade = A")
elif(sum>130) and (sum<140):
    print("grade = B")
elif(sum>120) and (sum<130):
    print("grade = C")
elif (sum > 110) and (sum < 120):
    print("grade = D")
elif (sum > 100) and (sum < 110):
    print("grade = D")
else:
    print("grade = F")