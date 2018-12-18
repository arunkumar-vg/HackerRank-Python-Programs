n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

l=0
uni=[]
for x in a:
    if x not in b:
        l+=1
for x in b:
    if x not in a:
        l+=1
print(l)
