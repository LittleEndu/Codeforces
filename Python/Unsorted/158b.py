input()
groups = [int(i) for i in input().split()]

amounts = {1: 0, 2: 0, 3: 0, 4: 0}
for i in groups:
    amounts[i] += 1

kill = min(amounts[1],amounts[3])
amounts[1]-=kill
amounts[3]-=kill
amounts[4]+=kill

kill = min(amounts[2],amounts[1]//2)
amounts[2]-=kill
amounts[1]-=kill*2
amounts[4]+=kill

if amounts[1]>0 and amounts[2]>0:
    amounts[1]-=1
    amounts[2]-=1
    amounts[3]+=1


amounts[4]+=amounts[1]//4
amounts[1]-=amounts[1]//4*4

if amounts[1]>1:
    amounts[amounts[1]] += 1
    amounts[1] = 0

amounts[4] += amounts[2]//2
amounts[2] -= amounts[2]//2*2

print(str(sum(amounts.values())))
