# Was smallest on submission!!!
# Previous best didn't alias and used .split()[1] instead of [-2:] and used range() instead of string multi
i=input
t,c=int(i()[-2:]),i()
for x in '_'*t:c=c.replace("BG","GB")
print(c)