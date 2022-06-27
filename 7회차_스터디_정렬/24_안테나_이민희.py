n = int(input())
pos = list(map(int,input().split()))
pos.sort()
if n%2==0:
    answer = n//2-1
else:
    answer = n//2
print(pos[answer])