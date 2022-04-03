n,m = map(int,input().split())
# print(m,n)
visited = [False] * n
def dfs(u,s):
    if s + n - u < m:
        return
    if s == m:
        for i in range(0,n):
            if visited[i]:
                print(i+1,end=' ')
        print()
        return
    if u == n:
        return
    visited[u] = True
    dfs(u+1,s+1)
    visited[u] = False
    dfs(u+1,s)
dfs(0,0)