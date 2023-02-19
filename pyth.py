a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter the 3rd number"))
print("the greatest number is")
if((a>b)and(a>c)):
    print(a)
elif((b>a)and(b>c)):
    print(b)
else:
    print(c)