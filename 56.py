n=input("Enter a string")
count=0
vowels={"a","A","e","E","i","I","o","O","u","U"}
for i in n:
    if(i in vowels):
        count=count+1
        
print("Total count of vowels is",count)    
