from math import ceil
inputs = [int(i) for i in input().split()]
print(ceil(inputs[0] / inputs[2]) * ceil(inputs[1] / inputs[2]))
