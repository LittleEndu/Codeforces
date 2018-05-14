# Smallest:
# a=int(input())+1
# while len(set(str(a)))<4:
#  a+=1
# print(a)

# Don't use if inside while loop....
# But, trick here was the +1 to input() so it acts as a "do while" loop

b=int(input())
while 1:
 b+=1
 if 4==len(set(str(b))):print(b);break
