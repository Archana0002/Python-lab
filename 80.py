import csv
with open("xyz.csv","r") as f:
    file=csv.DictReader(f)
    for line in file:
        if line:
            print(line['Name'],'\t',line['Department'],'\t',line['sem'],'\t',)
