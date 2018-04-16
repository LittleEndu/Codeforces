def sum_all_digits(nr):
    ss = 0
    while nr > 0:
        ss += nr % 10
        nr //= 10
    return ss


def first_digit(sumo_digits, bigger=0):
    if bigger != 0:
        real_first = first_digit(sumo_digits)
        while (real_first * 10 <= bigger):
            real_first *= 10
        if sumo_digits == 1:
            while (real_first * 10 <= (bigger - 1) * 10):
                real_first *= 10
    else:
        real_first = 0

    while (sum_all_digits(real_first) != sumo_digits or real_first < bigger):
        index = 0
        while sumo_digits - 9 >= sum_all_digits(real_first):
            real_first += 10 ** index * 9
            index += 1
        if (sum_all_digits(real_first) != sumo_digits or real_first < bigger):
            real_first += 1
    return real_first


def dumb(get_to, to_return=0):
    while (sum_all_digits(to_return) != get_to):
        to_return += 1
    return to_return


all_bb = []
for i in range(int(input())):
    all_bb.append(int(input()))

aa = 0
for bb in all_bb:
    aa += 1
    first = first_digit(bb, aa)

    if aa < first:
        aa = first

    while (sum_all_digits(aa) != bb):
        aa += 1
    print(aa)
