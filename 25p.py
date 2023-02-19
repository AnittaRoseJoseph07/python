list2=[]
k=int(input("enter the number of elements"))
for i in range(0,k):
    i=input()
    list2.append(i)
print(list2)
list1=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    i=input()
    list1.append(i)
print(list1)
print("colors present in list1 not list2")
c=list(set(list2).difference(list1))
print(c)