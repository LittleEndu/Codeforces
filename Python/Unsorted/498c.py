inputs = [int(i) for i in input().split()]
ll = inputs[0]
sod = inputs[1]
mn = -1
mx = -1

if ll == 1 and sod < 10:
    print("{} {}".format(sod, sod))

elif sod == 0:
    print("-1 -1")

elif ll < sod / 9:
    print("-1 -1")

elif ll == sod / 9:
    c = "9" * ll
    print("{} {}".format(c, c))

else:
    for smallnr in range(9):
        if (sod - smallnr) % 9 == 0:
            numbers = []
            while sod - smallnr - 9 > sum(numbers):
                numbers.append(9)
            numbers.append(sod - smallnr - sum(numbers))
            while numbers.count(0) > 0:
                numbers.remove(0)
            numbers.sort()
            mx = int(str(int("".join([str(i) for i in numbers]) + str(smallnr))).ljust(ll, "0"))
            if len(numbers) < ll - 1:
                if smallnr != 0:
                    numbers.append(smallnr - 1)
                else:
                    numbers[0]-=1
                numbers.sort()
                mn = int("1" + "".join([str(i) for i in numbers]).rjust(ll - 1, "0"))
            else:
                mn = int(str(smallnr) + "".join([str(i) for i in numbers]).rjust(ll - 1, "0"))
            numbers.reverse()
            break
    print("{} {}".format(mn, mx))
