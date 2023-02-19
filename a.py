n=int(input("enter the number of strings"))
print("enter the strings")
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