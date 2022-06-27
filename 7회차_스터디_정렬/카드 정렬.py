import heapq

n= int(input())

cards= [int(input()) for _ in range(n)]

cards.sort()
cards_heap = []
for i in range(n):
    heapq.heappush(cards_heap, cards[i])

sum=0
#for i in range(n):
#    sum+= ( cards[i] * (n-i) )

if n==1:
    print(1)
else:
    while len(cards_heap) > 1:
        x= heapq.heappop(cards_heap)
        y= heapq.heappop(cards_heap)
        sum+=x+y
        heapq.heappush(cards_heap, x+y)
    print(sum)
#print(sum - cards[0])