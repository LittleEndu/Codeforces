# Smallest
# k,n,w=map(int,input().split())
# print(max(0,w*(w+1)*k//2-n))


k,n,w=map(int,input().split())
print(-min(0,n-(w+w**2)//2*k))