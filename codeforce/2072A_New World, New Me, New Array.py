t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())
    if k > n * p or k < -n * p:
        print("-1")
    else:
        k = abs(k)
        p = abs(p)
        N = k // p
        if k <= N * p:
            print(N)
        else:
            print(N + 1)
