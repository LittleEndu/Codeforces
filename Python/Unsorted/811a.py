inputs = [int(i) for i in input().split()]


def candies(vladik_a, valera_a):
    amount = 0
    toggle = True
    while True:
        amount += 1
        if vladik_a < 0:
            return "Vladik"
        if valera_a < 0:
            return "Valera"
        if toggle:
            vladik_a -= amount
            toggle = False
        else:
            valera_a -= amount
            toggle = True

print(candies(inputs[0], inputs[1]))
