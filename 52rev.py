def rev(a):
    if not len(a):
        return ''
    else:
        return a[-1]+rev(a[:-1])

a=input("Enter a string:")
print("Reverse of a string is:", rev(a) )
