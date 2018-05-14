# Smallest:
# s=input();print([s.lower(),s.upper()][sum(map(str.isupper,s))>len(s)/2])

# map(str.isupper,s) instead of i.isupper()for i in s

s=input()
print([s.lower(),s.upper()][len(s)<2*sum(i.isupper()for i in s)])