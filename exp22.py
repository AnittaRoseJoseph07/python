dict={}
str=input("enter the string")
for i in str:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print("character frequency are")
for x,y in dict.items():
    print(x,y)