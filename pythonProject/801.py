n = int(input())
lt = list(map(int,input().split()))
def cntOne(n):
    cnt = 0
    while n:
        if n & 1:
            cnt += 1
        n >>= 1
    return cnt

for v in lt:
    print(cntOne(v),end=' ')

