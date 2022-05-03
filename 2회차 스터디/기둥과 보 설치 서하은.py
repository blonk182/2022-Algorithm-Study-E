def check(answer): # 구조물을 설치할 수 있는지(조건을 만족하는 구조인지) 확인  
    for x, y, stuff in answer: # answer 안에는 설치된 구조물들이 들어있음
        if stuff == 0: # 구조물이 기둥이라면
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 조건 만족
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False # 아니라면 False 반환
        elif stuff == 1: # 구조물이 보라면
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False # 아니라면 False 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame # list 요소값을 변수에 저장
        if operate == 1: # 구조물을 설치하는 경우
            answer.append([x, y, stuff]) # 일단 구조물 설치
            if not check(answer): # 구조 확인 후 설치가 불가능하다면
                answer.remove([x, y, stuff]) # 다시 구조물 삭제
        if operate == 0: # 구조물을 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 구조물 삭제
            if not check(answer): # 구조물 확인 후 삭제가 불가능하다면
                answer.append([x, y, stuff]) # 다시 구조물 설치
    return sorted(answer) # 정렬된 결과를 반환
