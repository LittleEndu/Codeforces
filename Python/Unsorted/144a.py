# Smallest
# input();*s,=map(int,input().split());a,b=s.index(max(s)),s[::-1].index(min(s))
# print(a+b-(len(s)-1-b<a))

# *s, instead of list()
# assignment using one =

n=input
n()
s=list(map(int,n().split()))
a=s.index(max(s))
b=s[::-1].index(min(s))
print(a+b-(a+b>=len(s)))