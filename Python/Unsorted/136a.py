# Gave up on code golfing this one....

ll = int(input())
friends = list(map(int, input().split()))
output = [0] * ll
for f in range(ll):
    output[friends[f] - 1] = f + 1
print(" ".join(map(str, output)))
