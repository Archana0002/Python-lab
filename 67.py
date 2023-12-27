import os
op=open("open.txt","a")
line=input("enter the line")
while(line):
    op.write("\n"+line)
    line=input("enter the line")
op.close()
