from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=len(a)*len(b)
ar=list(product(a,b))
for i in range(l):
    print((ar[i]),end=" ")