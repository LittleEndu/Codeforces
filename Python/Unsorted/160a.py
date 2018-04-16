# Smallest? possible
# i,o,x,y=0,0,input(),sorted(map(int,input().split()))
# while o<=sum(y)/2:o,i=o+y[~i],i+1
# print(i)

# while loop instead of function definition and two returns
# define all variables using one =
# [~i] instead of [::-1]

input()
def s():
 a=sorted(map(int,input().split()))[::-1]
 for i in range(len(a)):
  if sum(a[:i])>sum(a[i:]):
   return i
 return len(a)
print(s())