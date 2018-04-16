intin = int(input())
if intin == 2:
    print("NO")
elif intin%2==0:
    if intin%4==0:
        print("YES")
    elif (intin-2)%4==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")