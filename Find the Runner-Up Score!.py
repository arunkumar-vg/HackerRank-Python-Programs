n = int(input())
arr = list(map(int,input().split()))
s_max=0
x=0
a=sorted(arr)
mx=list(reversed(a))
lar=max(mx)
for i in range(0,n): 
    if(lar>mx[i]):
        print(mx[i])
        break

