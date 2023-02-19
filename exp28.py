def fact(num):
    print("factors are")
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
print("enter a number")
num=int(input())
fact(num)