n=int(input("enter number of colours you need in the list :"))
print("enter the elements ")
list1=[]
for i in range(0,n):
    ele=input()
    list1.append(ele)
print(list1)
m=int(input("enter number of colours you need in  second list :"))
print("enter the elements ")
list2=[]
for i in range(0,m):
    ele=input()
    list2.append(ele)
print(list2)
c=list(set(list1).difference(list2))
print(c)
