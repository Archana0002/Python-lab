import csv

field=['Name','Department','sem']
rows=[{'Name':'Archana','Department':'mca','sem':'s1'},{'Name':'Anu','Department':'mca','sem':'s1'}]

with open('xyz.csv','w') as f:
    writer=csv.DictWriter(f,fieldnames=field)
    writer.writeheader()
    writer.writerows(rows)
    f.close()
