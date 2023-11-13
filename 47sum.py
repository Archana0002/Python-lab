def sum_n(n):
    if not n:return 0
    else: return n + sum_n(n-1)
n=int(input("Enter number:"))
