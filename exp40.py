import csv
with open("desp.csv")as f:
    d=csv.DictReader(f)
    print("Subject Group")
    for i in d:
        print(i['Period'])

