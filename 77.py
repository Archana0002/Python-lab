import csv

field=['Name','Dept','sem']
row=[['Archana','Mca','S1'],['Abi','Mca','S1']]

with open('abc.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(field)
    writer.writerows(row)
    f.close()
