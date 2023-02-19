str=input("Enter string : ")
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print("The character frequency:")
for m,n in dict.items():
 print(m,n)
