# 1. 실수 수정 버전
def solution(numLog):
    
    result = ""  # 🔧 결과 문자열
    
    for i in range(1, len(numLog)):  # 🔧 1부터 시작 (이전 값과 비교해야 하므로)
        
        diff = numLog[i] - numLog[i - 1]  # 🔧 변화량 계산
        
        if diff == 1:
            result += "w"
        elif diff == -1:
            result += "s"
        elif diff == 10:
            result += "d"
        elif diff == -10:
            result += "a"
    
    return result


# 2. 개선된 추천 스타일
def solution_pythonic(numLog):
    
    result = []
    
    for i in range(1, len(numLog)):
        
        diff = numLog[i] - numLog[i - 1]
        
        if diff == 1:
            result.append("w")
        elif diff == -1:
            result.append("s")
        elif diff == 10:
            result.append("d")
        elif diff == -10:
            result.append("a")
    
    return "".join(result)  # 리스트 → 문자열 변환



# 내가 틀리기 쉬운 부분 정리

# [실수 1] 값 자체를 비교함
# c = numLog(i)
# if c == 1:
# 👉 이 문제는 값이 아니라 "변화량"을 봐야 함
# 👉 numLog[i] - numLog[i-1]


# [실수 2] 리스트 접근 문법 오류
# numLog(i)
# 👉 함수 호출 형태 → 오류
# 👉 numLog[i] 로 접근해야 함


# [실수 3] 반복 시작 위치
# range(len(numLog))
# 👉 i=0일 때 이전 값 없음
# 👉 range(1, len(numLog))로 시작해야 함


# [실수 4] 결과를 저장하지 않음
# c = "w"
# 👉 변수 c만 바뀌고 누적이 안됨
# 👉 result += "w" 또는 append 필요


# [실수 5] return numLog
# 👉 문제는 문자열을 요구함
# 👉 result를 반환해야 함


# [실수 6] str(numLog)
# 👉 리스트를 문자열로 바꾸면 "[0,1,...]" 형태
# 👉 원하는 결과 "wsda..." 아님


# [실수 7] 문자열 따옴표 없음
# c = w
# 👉 NameError 발생
# 👉 반드시 "w"


# 핵심 개념 정리

# 1. 변화량(diff) 계산
# diff = numLog[i] - numLog[i-1]

# 2. 문자열 누적
# result += "w"

# 3. 리스트 → 문자열 변환
# "".join(list)

# 4. 반복 시작은 1부터
# 이전 값과 비교해야 하기 때문