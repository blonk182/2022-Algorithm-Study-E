n, m = map(int,input().split())    # n = 볼링공 개수, m = 볼링공 최대 무게
balls = list(map(int,input().split()))  # 1번 ~ n번까지 공 각각의 무게 배열로 저장

cases = len(balls) * (len(balls)-1) / 2 # 서로 같은 무게의 공을 선택하는 경우까지 포함한 전체 경우의 수

balls_set = list(set(balls)) # 중복 제거

for ball in balls_set:
    count = balls.count(ball)
    if count > 1:  # 만약 같은 무게의 다른 공이 더 있다면
        cases -= count * (count-1) / 2  # 서로 같은 무게의 공을 선택하는 경우의 수를 전체에서 제거

print(int(cases))

# 1, 3, 2, 3, 2, 2, 4
# 1, 3, 2, 4