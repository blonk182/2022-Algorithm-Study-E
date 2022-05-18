n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for i in range(len(coins)):
    if target < coins[i]:
        break
    else:
        target += i
print(target)

# target = 1 2 4 8 16 32 ..
# 1 있으면 1 만들 수 있고
# 1, 2 있으면 3 만들 수 있고
# 1, 2, 4 있으면 3, 5, 6 만들 수 있고
# 1, 2, 4, 8 있으면 7, 8, 9, 10, 11, 12, 13, 14, 15 만들 수 있고
# 1, 2, 4, 8, 16 있으면 ...., 30, 31 만들 수 있고
# ...
