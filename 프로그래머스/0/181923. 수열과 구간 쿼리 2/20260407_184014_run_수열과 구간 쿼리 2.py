# 1. 실수 수정 버전
def solution(arr, queries):
    
    answer = []
    
    for s, e, k in queries:
        
        temp = []  # 🔧 조건을 만족하는 값들 저장
        
        for i in range(s, e + 1):  # 🔧 인덱스 범위 순회
            
            if arr[i] > k:  # 🔧 k보다 큰 값만
                temp.append(arr[i])
        
        if temp:  # 🔧 값이 존재하면
            answer.append(min(temp))  # 가장 작은 값 추가
        else:
            answer.append(-1)  # 없으면 -1
    
    return answer


# 2. 개선된 추천 스타일
def solution_pythonic(arr, queries):
    
    answer = []
    
    for s, e, k in queries:
        
        # 🔥 슬라이싱 + 조건 필터
        candidates = [x for x in arr[s:e+1] if x > k]
        
        answer.append(min(candidates) if candidates else -1)
    
    return answer



# 내가 틀리기 쉬운 부분 정리

# [실수 1] i를 값으로 사용
# for i in arr:
# if s <= i <= e
# 👉 i는 값 (0,1,2...)이지 인덱스가 아님
# 👉 인덱스는 range(s, e+1)로 돌아야 함


# [실수 2] arr[i] 접근 오류
# for i in arr:
# arr[i]
# 👉 i가 값이면 arr[i]는 엉뚱한 위치 접근


# [실수 3] return을 반복문 안에서 사용
# return answer += ...
# 👉 첫 번째 반복에서 함수 종료됨
# 👉 반드시 for문 밖에서 return


# [실수 4] += 사용 방식 오류
# answer += arr[i]
# 👉 리스트에는 append() 사용해야 함


# [실수 5] 조건 잘못 이해
# arr[i] >= k
# 👉 문제는 "k보다 큰 값"
# 👉 arr[i] > k


# [실수 6] 최소값 구하는 방식 오류
# min(arr[i])
# 👉 arr[i]는 숫자 → min 불가능
# 👉 여러 값 모아서 min(temp)


# [실수 7] 문자열 "-1"
# 👉 결과는 정수 -1이어야 함


# [실수 8] .min 사용
# arr[i].min
# 👉 존재하지 않는 속성 (AttributeError)


# 핵심 개념 정리

# 1. 인덱스 범위 순회
# for i in range(s, e+1)

# 2. 조건 필터링
# if arr[i] > k

# 3. 최소값 찾기
# min(리스트)

# 4. 값 없을 때 처리
# if temp: else -1

# 5. 슬라이싱
# arr[s:e+1]