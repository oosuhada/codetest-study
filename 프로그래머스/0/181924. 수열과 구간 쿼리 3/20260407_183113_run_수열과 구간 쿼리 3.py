# 1. 실수 수정 버전
def solution(arr, queries):
    
    for i, j in queries:  # 🔧 수정: queries(i,j) → queries
        
        temp = arr[i]      # 🔧 swap을 위한 임시 변수
        arr[i] = arr[j]
        arr[j] = temp
    
    return arr


# 2. 개선된 추천 스타일
def solution_pythonic(arr, queries):
    
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]  # 🔥 파이썬 swap (핵심)
    
    return arr



# 내가 틀리기 쉬운 부분 정리

# [실수 1] queries(i, j) 사용
# for i,j in queries(i,j):
# 👉 함수 호출 형태 → 오류
# 👉 queries는 리스트이므로 그대로 순회해야 함
# 👉 for i, j in queries


# [실수 2] 리스트 접근 () 사용
# arr(i)
# 👉 함수 호출 → 오류
# 👉 arr[i] 로 접근해야 함


# [실수 3] swap 방법 모름
# arr(i) <-> arr(j)
# 👉 파이썬에서는 이런 문법 없음


# [실수 4] arr2 = arr (참조 문제)
# arr2 = arr
# 👉 같은 리스트를 가리킴 (복사 아님)
# 👉 arr2 바꾸면 arr도 같이 바뀜


# [실수 5] 잘못된 순회 방식
# for i,j in queries[i,j]
# 👉 문법 오류
# 👉 리스트 자체를 순회해야 함


# [실수 6] swap 로직 오류
# arr[i] = arr2[j]
# arr[j] = arr2[i]
# 👉 arr2가 같은 리스트라 값이 꼬일 수 있음


# 핵심 개념 정리

# 1. 리스트 순회 (2차원 배열)
# for i, j in queries

# 2. 리스트 인덱스 접근
# arr[i]

# 3. swap 방법 2가지

# (1) 기본 방식
# temp = arr[i]
# arr[i] = arr[j]
# arr[j] = temp

# (2) 파이썬 방식 (추천)
# arr[i], arr[j] = arr[j], arr[i]

# 4. 참조 vs 복사
# arr2 = arr → 같은 객체 (복사 아님)
# arr2 = arr[:] → 복사