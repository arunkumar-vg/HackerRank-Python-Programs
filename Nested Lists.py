num = int(input())

name=[]
mark=[]
a=0
temp=0
for i in range(0, num):
    n_val = input()
    name.append(n_val)
    m_val = float(input())
    mark.append(m_val)
mini=min(mark)
maxi=max(mark)

for i in range(0, num):
    if(mark[i]<=maxi and mark[i]!=mini):
        maxi=mark[i]
        temp=i
val=[]
val.append(name[temp])
l=maxi
a+=1
for i in range(0, num):
    if(l==mark[i] and name[i]!=val[0]):
        val.append(name[i])
        a+=1
b=[]
b=sorted(val)
for i in range(0, a):
    print(b[i])