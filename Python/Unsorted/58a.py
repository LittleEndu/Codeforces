# import re;print("YES"if re.search("h.*e.*l.*l.*o",input())else"NO")
# self f** explanatory. One day I'll learn regex

dd = {i: [] for i in "helo"}
a = "".join(i for i in input() if i in "helo")
for i in range(len(a)):
    for j in "helo":
        if a[i] == j:
            dd[j].append(i)
s = 0


def solve():
    for h in dd['h']:
        for e in dd['e']:
            for l in dd['l']:
                for ll in dd['l']:
                    for o in dd['o']:
                        if h < e < l < ll < o:
                            print("YES")
                            return
    print("NO")


solve()
