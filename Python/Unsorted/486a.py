# Smallest:
# n=int(input())
# print(n//2-n%2*n)

# ...

# Could have saved 3 chars anyway

i=int
a=i(input())
b=i(a/2+0.5)
print((-1)**(a%2)*b)