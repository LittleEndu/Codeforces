# Smallest:
# i=input;print('YNEOS'[any(map(sum,zip(*[map(int,i().split()) for x in ' '*int(i())])))::2])

# alias for input
# map sum instead of for loop
# 'yn'[any()::2] instead of ['n','y'][[0,0,0]==[0,0,0]]
# Also input for for loop's iteration is called before for loop's body...

a=int(input())
print(['NO','YES'][[sum(i) for i in zip(*[map(int,input().split()) for n in "a"*a])]==[0,0,0]])