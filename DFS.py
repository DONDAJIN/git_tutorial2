#DFS(再帰を用いた実装)
import sys
sys.setrecursionlimit(10**7)
h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]

def dfs(x,y):
    if not (0<=x<h) or not(0<=y<w) or c[x][y]=='#':
        return 
    
    if c[x][y]=='g':
        print('Yes')
        exit()
    
    c[x][y]='#'
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    
for i in range(h):
    for j in range(w):
        if c[i][j]=='s':
            si,sj=i,j
dfs(si,sj)
print('No')
