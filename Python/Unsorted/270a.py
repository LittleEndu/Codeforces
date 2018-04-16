inputs = []
for i in range(int(input())):
    inputs.append(int(input()))

for i in inputs:
    sides = 3
    angle = 60
    while angle <= i:
        if angle == i:
            print("YES")
            break
        sides += 1
        angle = 180 * (sides - 2) / sides
    if angle!=i:
        print("NO")
3