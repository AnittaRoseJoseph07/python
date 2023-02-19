list1=[45,89,87,67,90]
list2=[89,77,66,55,34]
a=len(list1)
b=len(list2)
c=sum(list1)
d=sum(list2)
if(a==b):
    print("two list are of same length")
else:
    print("two list are not of same length")
if(c==d):
    print("sum of list are same")
else:
    print("sum of list are not same")
for i in list1:
    for j in list2:
        if(i==j):
            print(i)

