amount = 0
for i in range(int(input())):
    ss = input()
    if "+" in ss:
        amount += 1
    else:
        amount -= 1
print(str(amount))
