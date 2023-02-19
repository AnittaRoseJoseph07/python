n=int(input("enter the no. of strings"))
print("enter the elements")
list=[]
for i in range(0,n):
    ele=input()
    count=0
    list.append(ele)
print(list)
for i in list:
    for j in i:
        if j=='a':
            count=count+1
print(count)
