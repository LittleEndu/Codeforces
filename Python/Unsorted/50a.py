def get_max_dominoes(n,m):
    if n==1 and m==1:
        return 0
    if m==2:
        return n
    if n==2:
        return m
    if m>n:
        return n + get_max_dominoes(n,m-2)
    return m + get_max_dominoes(n-2,m)

size = [int(i) for i in input().split()]
print(get_max_dominoes(size[0],size[1]))