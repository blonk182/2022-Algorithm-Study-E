s=input()

# 연속이 아닐경우 일단 다 뒤집는다 가정하고 적게 뒤집는걸 답으로 도출

cnt0=0         #1 =>0 으로 바꾸기 위한 카운트
cnt1=0         #0 =>1 으로 바꾸기 위한 카운트



if s[0]== '1':
    cnt0+=1         
else :
    cnt1+=1


for i in range(0, len(s)-1):        #마지막 인덱스는 빼야하니까 -1
    if s[i] != s[i+1]:
        if s[i+1]=='1':
            cnt0 +=1
        else:
            cnt1+=1

print(min(cnt0,cnt1))

print(cnt0, cnt1)
