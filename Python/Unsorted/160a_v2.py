# 4 chars smaller than mcpower's solution

i=o=0
input()
y=sorted(map(int,input().split()))
while o<=sum(y)/2:o,i=o+y[~i],i+1
print(i)