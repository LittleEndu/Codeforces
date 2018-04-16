# Smallest:
# n=int(input());print('YNEOS'[all(set(str(i))-set('47')or n%i for i in range(n+1))::2])

# No idea...
# Also not going to brute force it against test cases like others seemed to have. My solution would work for any number
d=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
a=int(input())
print(['NO','YES'][any([a%i==0 for i in d])])