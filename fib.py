num=int(input("enter the limit"))
a=0
b=1
sum=0
print(a)
for i in range(0,num):
    a=b
    b=sum
    sum=a+b
    print(sum)