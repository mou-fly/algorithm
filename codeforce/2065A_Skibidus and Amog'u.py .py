n = int(input())
for _ in range(n):
    string = str(input())
    if len(string) == 2:
        print("i")
    else:
        ans = ""
        for i in range(len(string)-2):
            ans += string[i]
        ans += "i"
        print(ans)