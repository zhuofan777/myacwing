a, b, p = map(int, input().split())
ans = 1 % p
while b:
    if b & 1:
        ans = ans * a
        ans = ans % p
    b >>= 1
    a = a * a
    a = a % p
print(ans)
