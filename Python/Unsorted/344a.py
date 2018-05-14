# Pretty good, but I golfed the top one even more

n=input
s="".join(n()for _ in"_"*int(n()))
print(s.count("00")+s.count("11")+1)