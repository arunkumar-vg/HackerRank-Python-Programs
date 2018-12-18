from collections import defaultdict
n=(int(input()))
if 1<=n<=10**5: 
 
    d=defaultdict(int)

    for i in range(n):
        key=input()
        d[key] +=1
    print(len(d.keys())) 
    x=(d.values())
    print(*x)
