x=int(input("enter the starting year"))
y=int(input("enter the ending year"))
print("leap years are")
for i in range(x,y):
    if(i%4==0):
        print(i)