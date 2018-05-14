# Bright minds think alike
# Actually got to the same solution after failing to see that you can't just look and one slice, you need to look at all

l=lambda:map(int,input().split())
n,m=l()
f=sorted(l())
print(min(f[i+n-1]-f[i]for i in range(m-n+1)))