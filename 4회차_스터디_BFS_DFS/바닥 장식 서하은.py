N, M = map(int, input().split())
cnt = 0
a = []
b = []
for k in range(M):
    b.append("!")

for i in range(N):
    a = str(input())
    for j in range(len(a)):
        if a[j] == '-':
            if j != (M-1): 
                if a[j] == a[j+1]:
                    pass
                else:
                    cnt += 1
            else:
                cnt += 1
        if a[j] == '|':
            if a[j] == b[j]:
                pass
            else:
                cnt += 1
    b = a
print(cnt)