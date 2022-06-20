n = int(input())
numbers = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split()) # 각 연산자 +-*/ 개수

minn = 1e9 # 1*10^9
maxx = -1e9


def dfs(i, now):
    global minn, maxx, add, sub, mul, div
    if i == n:
        minn = min(minn, now)
        maxx = max(maxx, now)
        return
    else:
        if add>0:
            add-=1
            dfs(i+1, now+numbers[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1, now-numbers[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1, now*numbers[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1, now//numbers[i])
            div+=1

dfs(1, numbers[0])

print(maxx)
print(minn)

