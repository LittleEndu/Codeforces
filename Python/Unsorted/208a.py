# print(*input().split('WUB'))
# And I thought regex is going to beat me...
# Wait.... the checker doesn't care about double space......................
# Now I stand by my solution, even thought it would replace "WUBWWUBUWUBBWUB" with ""
def l(a):
 for b in ['WUB','  ']:a=a.replace(b,' ')
 return a
w=input()
while w!=l(w):w=l(w)
print(w.strip())