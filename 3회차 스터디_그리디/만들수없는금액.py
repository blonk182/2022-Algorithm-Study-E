n=int(input())
m = list(map(int, input().split()))
m.sort()

target=1

for i in m:            
    if target <i: 
        break
    target +=i
print(target)


#1 1 3 5

# 1, 2, 3, 4, 5, 6, ... 11=answer


# 1 2 3 8

# 1,3 4, 5, 6, 7=answer