def solve():
    ss = input()
    while len(ss) > 6:
        if ss[:7] in ["0000000", "1111111"]:
           return "YES"
        else:
            ss = ss[1:]
    return "NO"
print(solve())