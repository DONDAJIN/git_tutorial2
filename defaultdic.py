#defaultdic
n,m=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
from collections import defaultdict
flag=defaultdict(int)
for i in range(n):
    flag[T[i]]=1
for j in range(m):
    if flag[S[j]]==1:
        print('Yes')
    else:
        print('No')
#While を使っても以下のように出来る。
currentpos=0
for st in T:
    if S[currentpos]==st:
        print('Yes')
        currentpos=+1
        break
    else:
        print('No')
        currentpos=+1
print('uno')

