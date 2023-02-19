n=int(input("enter a number"))
for i in range(0,n+1):
    for j in range(1,i+1):
        square=i*j
        print(square,end=" ")
    print("\r")
