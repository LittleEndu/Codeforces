amount = 0
for i in range(int(input())):
    if sum([int(i) for i in input().split()]) > 1:
        amount+=1
print(str(amount))