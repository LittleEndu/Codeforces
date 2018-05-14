# Smallest:
# print('NYOE S'[sum([i in'47'for i in input()])in(4,7)::2])

# in keyword and sum() instead of count (gets rid of double count())
# 'NYOE S'::2 -.-
# in (4,7) instead of checking each individually (missed because I thought divisible by 4,7 instead of == 4,7
#       and missed it after changing it)

a=input()
b=a.count('4')+a.count('7')
print(['NO','YES'][(b==4 or b==7) and b!=0])