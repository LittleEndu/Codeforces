place_needed = int(input().split()[1])
scores = [j for j in reversed(sorted([int(i) for i in input().split() if int(i) > 0]))]
try:
    score_needed = scores[place_needed - 1]
except IndexError:
    score_needed = 0
amount = 0
for i in scores:
    if i >= score_needed:
        amount += 1
print(amount)
