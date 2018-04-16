# No need for int because 1,2,3 will always sort correctly
# ::2 instead of split because there won't be anything else besides 1 length digits
# So smallest solution is:
# print("+".join(sorted(input()[::2])))
print("+".join(map(str,sorted(map(int,input().split("+"))))))