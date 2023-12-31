import csv
with open('abc.csv','r') as f:
    file=csv.reader(f)

    for i in file:
        if i: print(i[0],'\t',i[1],'\t',i[2])
 
