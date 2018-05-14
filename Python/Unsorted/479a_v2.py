# Smallest. Only need ot consider cases with 1, other wise a*b*c is always the biggest

a,b,c=[int(input()) for i in "___"]
print(max(a*b*c,a*(b+c),(a+b)*c,a+b+c))