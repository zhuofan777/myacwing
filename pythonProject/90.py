a = int(input())
b = int(input())
p = int(input())

res = 0
while b:
    if b & 1:
        res = (res + a) % p
    b = b >> 1
    a = (a + a) % p
print(res)
