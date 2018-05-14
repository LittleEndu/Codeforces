a=input("Input string:")
b=input("Input the other string:")
c=zip(a.ljust(len(b)),b.ljust(len(a)))
print("".join(["".join(i) for i in c]))
