n = int(input())

visited = [False] * n

def dfs(a):
    if a == n:
        for i in range(len(visited)):
            if visited[i]:
                print(i+1,end=" ")
        print()
        return
    visited[a] = False
    dfs(a+1)
    visited[a] = True
    dfs(a+1)


dfs(0)