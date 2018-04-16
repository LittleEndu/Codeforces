# Smallest:
# n=input()
# print([n,n.swapcase()][n[1:].upper()==n[1:]])

# Didn't know swapcase() existed
# bool == int, so use index instead of ternary

a=input();print((a.capitalize() if a[0].islower() else a.lower()) if a[1:]==a[1:].upper() else a)