square=lambda n:n*n
rect=lambda l,b:l*b
tri=lambda base,h:1/2 * base *h

n=int(input("Enter side of square"))
print("Area of square is",square(n))

l=int(input("Enter length of rectangle"))
b=int(input("Enter breadth of rectangle"))
print("Area of rectangle is",rect(l,b))

base=int(input("Enter base of triangle"))
h=int(input("Enter height of triangle"))
print("Area of triangle is",tri(base,h))



