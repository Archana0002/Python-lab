def str(n):
    for i in range(len(n)):
        if n[i]>100:
            n[i]="Over"
    return n


n=input("Enter the list of numbers seperated by space")
n=list(map(int,n.split()))
print("Numbers are",str(n))
