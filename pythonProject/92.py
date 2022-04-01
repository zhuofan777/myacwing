# 确定参数
# 当前在哪一层-当前考虑的是第几个数 u
# 前面的数有没有选 bool[]

n = int(input())


# st = [False] * (n+10)

def dfs(u, state):
    if u == n:
        for i in range(0, n):
            if state >> i & 1:
                print(i + 1, end=" ")
        print()
        return
    dfs(u + 1, state)
    dfs(u + 1, state | 1 << u)


dfs(0, 0)
