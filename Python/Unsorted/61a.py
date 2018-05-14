# Smallest:
# i=input;print(''.join('01'[a!=b]for a,b in zip(i(),i())))

# zip()...

n,i=input,int
l=lambda a:i("0b"+a,2)
x,y=n(),n()
p=len(x)
print(bin(l(x)^l(y))[2:].rjust(p,"0"))