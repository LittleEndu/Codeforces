# Smallest:
# n=int(input())
# x=[6,4,8][n%3]
# print(x,n-x)

# Probably could have realized that

i=int(input())
a=4
while (i-a)%6in[1,5]:a+=2
print(a,i-a)