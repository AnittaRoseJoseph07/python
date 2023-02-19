num=int(input("enter the limit : "))
list1=[]
for i in range(num):
    a=int(input("enter the element : "))
    list1.append(a)5

newlist=[i*i for i in list1 if i>0]
print("the squares are",newlist)


