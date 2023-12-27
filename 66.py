import os
op=open("open.txt","r")
ls=op.readlines()
op.close()
op2=open("copy.txt","w")
op2.writelines(ls)
op2.close()
