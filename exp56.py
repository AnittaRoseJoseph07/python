str=input("enter the line of text")
dict={}
x=str.split()
print(x)
for i in x:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print("character frequency")
for x,y in dict.items():
    print(x,y)
