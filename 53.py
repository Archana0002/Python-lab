import math
n=9999
l=list()
for i in range(1000,n):
    if(math.sqrt(i)==int(math.sqrt(i))):
        temp=str(i)
        if(int(temp[0])%2==0 and int(temp[1])%2==0 and int(temp[2])%2==0 and int(temp[3])%2==0 and temp[0]!="0" and temp[1]!="0" and temp[2]!="0" and temp[3]!="0"):
            print(i)
            l.append(i)
print(i)
        

