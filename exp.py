import csv
field=['id','name','age']
data=[{'id':44,'name':'anitta','age':15},
{'id':45,'name':'abhiya','age':56}]
try:
with open("name.csv",'w')as f:
write=csv.DictWriter(f,fieldnames=field)
write.writeheader()
for i in data:
write.writerow(i)
except IOError:
print("input output error")
d=csv.DictReader(open("name.csv"))
print("csv file output")
for i in d:
print(i)