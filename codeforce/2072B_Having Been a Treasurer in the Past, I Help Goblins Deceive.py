t = int(input())
for _ in range(t):
    l = int(input())
    string = str(input())
    cnt_bot = string.count("_")
    cnt_mid = string.count("-")
    if cnt_mid < 2 or cnt_bot < 1:
        print(0)
    else:
        left = int(cnt_mid / 2)
        right = cnt_mid - left
        # print(left,right)
        print(left * right * cnt_bot)


