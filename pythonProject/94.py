n = int(input())
visited = [False]*n
ans = []
def dfs(s):
    if s == n:
        for i in ans:
            print(i + 1,end=" ")
        print()
        return
    for i in range(0,n):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            dfs(s+1)
            ans.pop(-1)
            visited[i] = False
dfs(0)
