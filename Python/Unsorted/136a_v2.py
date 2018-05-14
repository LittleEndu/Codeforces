# Smallest
# z=input;i=int
# a=[0]*i(z())
# for x,y in enumerate(z().split()):
# 	a[i(y)-1]=i(x)+1
# print(*a)

# enumerate instead of range(length)
# then you don't need to save length
# didn't know print(*output) would work just fine

q,w,m=int,input,map
l,f=q(w()),list(m(q, w().split()))
o=[0]*l
for i in range(l):o[f[i]-1]=i+1
print(" ".join(m(str,o)))
