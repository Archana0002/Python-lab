l=input("Enter the numbers")
l=list(map(int,l.split()))
print(l)
d1={}
for i in l:
    d1[i]=d1.get(i,0)+1

n=int(input("Enter element to search:"))
print(n,"appears",d1[n],"times")

