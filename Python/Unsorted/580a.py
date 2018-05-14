# Smallest

i=input
i()
c=m=l=0
for n in i().split():
 n=int(n)
 c=c+1 if n>=l else 1
 m=max(m,c)
 l=n
print(m)