n = int(input()) 
unit = list(map(int, input().split())) 
unit.sort() 

result = 1 

for i in unit: 
  if result < i: 
    break 
  
  result = result + i 

print(result)

