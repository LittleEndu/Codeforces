amount = int(input())
for i in range(amount):
    ss = input()
    if len(ss)>10:
        print("{}{}{}".format(ss[0],len(ss)-2,ss[-1]))
    else:
        print(ss)