n = int(input())
coin = list(map(int,input().split()))  
coin.sort()

target = 1

for i in coin:
    if target < i: # target-1 까지 만들 수 있음
        break
    target += i

print(target)


# target = 1
# → 우리에게는 1원이 있다.
# → target 갱신 = 1 + 1 (1까지의 모든 금액을 만들 수 있다.)

# target = 2
# → 우리에게는 2원이 있다.
# → target 갱신 = 2 + 2 (3까지의 모든 금액을 만들 수 있다.)

# target = 4
# → 우리에게는 3원이 있다.
# → target 갱신 = 4 + 3 (6까지의 모든 금액을 만들 수 있다.)

# target = 7
# → 7원보다 작은 동전들로는 6원까지밖에 못 만들며, 남은 건 7원보다 큰
# 8원밖에 없다. 그래서 1, 2, 3, 8원으로 만들 수 없는 금액의 최솟값은 7원이다.