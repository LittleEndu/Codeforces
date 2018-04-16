#Smallest:
# for i in range(5):
#   s=input()
#   if '1' in s:
#     print(abs(i-2)+abs(s.index('1')//2-2))

# print out instead of store variable
# use //2 instead of split()

x = y = 0
for i in range(5):
    a = input()
    if "1" in a:
        y = abs(i - 2)
        x = abs(a.split().index("1") - 2)
print(x+y)
