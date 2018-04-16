# Smallest:
# m=k=0
# for i in range(int(input())):k-=eval(input().replace(' ','-'));m=max(m,k)
# print(m)

# Same stuff more elegant. eval() is used instead of split()
# k is the current count, m is the max of count.

count = [0]
for n in range(int(input())):
    i, o = map(int, input().split())
    count.append(count[-1]-i+o)
print(max(count))
