inputs = [int(i) for i in input().split()]
marks = [int(i) for i in input().split()]


def is_k(ss, req, aa, ll):
    ss += req * aa
    avg = ss / (ll + aa)
    kk = round(avg)
    return kk == req or avg == req - 0.5


sss = sum(marks)
lll = len(marks)
aaa = 0
while not is_k(sss, inputs[1], aaa, lll):
    aaa += 1

print(aaa)
