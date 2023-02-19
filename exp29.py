for i in range(1000,10000):
    i=int(input("enter a number"))
    num=int(math.sqrt(i))
    if(num*num==i):
        n=i
        while(n!=0):
            r=n%10
            n=n/10
        if(r%2!=0):
            break
            else:
            print(i)