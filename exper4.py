txt=input('enter the text : ')
txt1=txt.split(" ")
print(txt1)
dic={}
for n in txt1:
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1
for m,n in dic.items():
    print(m,n)
