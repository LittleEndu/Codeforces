# Smallest possible: r=input;r();c=r();print(sum(p==n for p,n in zip(c[1:],c)))

# alias for input
# zip() instead of previous
# sum() and == instead of initial
# print the sum() instead of storing variable
initial = int(input())
previous = None
for i in input():
    if i != previous:
        initial -= 1
    previous = i
print(initial)