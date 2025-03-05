t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 3
    k = 15
    N = n // k
    n -= N * k
    ans = cnt * N + 1
    if n == 1:
        ans += 1
    elif n >= 2:
        ans += 2
    print(ans)
