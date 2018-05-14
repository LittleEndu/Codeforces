# *k,d=[int(input())for _ in ' '*5];print(sum(1-all(x%m for m in k)for x in range(1,d+1)))

# *k,d ... didn't know this would work
# Count damaged dragons not all dragons - dragons who got away unharmed
# all not 0 ... great shortcut

i=lambda:int(input())
a=[i(),i(),i(),i()]
d=i()
r=range
s=set
x=s(r(1,d+1))
b=[s(r(f,d+1,f)) for f in a]
for c in b:x=x-c
print(d-len(x))