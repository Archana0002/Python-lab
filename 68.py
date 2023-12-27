import os
op=open("open.txt","r")
ls=op.readlines()
ls2=ls[::2]
op.close()
op2=open("copyodd.txt","w")
op2.writelines(ls2)
op2.close()
