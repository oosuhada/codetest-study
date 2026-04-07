# 1. 실수 수정 버전
def solution(n, control):
    
    for i in range(len(control)):
        
        c = control[i]  # 🔧 수정: i는 인덱스 → 실제 문자 꺼내기
        
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        elif c == "a":
            n -= 10
    
    return n


# 2. 개선된 추천 스타일
def solution_pythonic(n, control):
    
    for c in control:  # 문자열 직접 순회
        
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        elif c == "a":
            n -= 10
    
    return n



# 내가 틀리기 쉬운 부분 정리

# [실수 1] i를 문자로 착각
# for i in range(len(control)):
# if i == "w":
# 👉 i는 0,1,2 같은 숫자 (인덱스)
# 👉 해결: control[i]로 실제 문자 꺼내야 함


# [실수 2] range(len(control)-1)
# 👉 마지막 문자 하나가 아예 실행 안됨
# 👉 문자열 전체 돌려야 하므로 len(control) 사용


# [실수 3] range(0, len(control))
# 👉 동작은 맞지만 불필요하게 복잡
# 👉 그냥 range(len(control)) 또는 for c in control 사용


# [실수 4] 반복문 밖에서 i 사용
# if i = len(control)
# 👉 문법 오류 (= 대신 == 필요)
# 👉 애초에 이 조건 자체가 필요 없음


# [실수 5] 조건문 위치 오류
# 반복문 끝나고 조건 검사하려고 함
# 👉 이 문제는 "매 반복마다 n 변경"이 핵심


# 핵심 개념 정리

# 1. 문자열 순회 방법
# for c in control  ← 가장 파이썬스러움

# 2. 인덱스 vs 값
# i → 인덱스 (0,1,2...)
# control[i] → 실제 문자

# 3. 반복문은 전체 길이만큼 돌아야 함
# len(control) 사용

# 4. 조건은 반복문 안에서 처리
# 한 글자씩 처리하는 문제 구조