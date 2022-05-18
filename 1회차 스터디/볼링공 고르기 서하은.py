N, M = map(int, input().split())
n_list = list(map(int, input().split(" ")))
cnt = 0

for i in range(N-1):
    for j in range(i+1, N):
        if n_list[i] != n_list[j]: #n_list[i] : 기준이 되는 볼링공
            cnt += 1

print(cnt)