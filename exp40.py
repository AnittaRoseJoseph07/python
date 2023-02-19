import csv
with open('dep.csv')as f:
    d=csv.DictReader(f)
    for i in d:
        print(i)

