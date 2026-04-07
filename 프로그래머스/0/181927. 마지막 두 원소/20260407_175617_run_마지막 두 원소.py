# 1. 실수 수정 버전
def solution(num_list):
    
    n = len(num_list)
    
    # 🔧 수정: 마지막 / 이전 원소 인덱스
    last = num_list[n - 1]
    secondLast = num_list[n - 2]
    
    # 🔧 수정: 문자열 제거 + 실제 계산
    if last > secondLast:
        return num_list + [last - secondLast]  # 리스트 + 리스트
    else:
        return num_list + [2 * last]


# 2. 개선된 추천 스타일
def solution_pythonic(num_list):
    
    last = num_list[-1]          # 마지막 원소
    second_last = num_list[-2]   # 이전 원소
    
    if last > second_last:
        num_list.append(last - second_last)
    else:
        num_list.append(last * 2)
    
    return num_list



# 🔴 내가 틀린 부분 정리

# ❌ [실수 1] 인덱스 범위 초과
# last = num_list[len(num_list)]
# 👉 IndexError 발생
# 👉 마지막 인덱스는 len(num_list) - 1

# ❌ [실수 2] 이전 원소 접근 실수
# secondLast = num_list[len(num_list)-1]
# 👉 이건 마지막 원소임 (이전 원소 아님)
# 👉 이전 원소는 len(num_list) - 2

# ❌ [실수 3] return에서 += 사용
# return num_list += 값
# 👉 문법 오류 (SyntaxError)
# 👉 append() 또는 + [값] 사용

# ❌ [실수 4] 리스트 + 문자열
# num_list + "last - secondLast"
# 👉 TypeError 발생 (자료형 불일치)

# ❌ [실수 5] 계산을 문자열로 작성
# "last - secondLast"
# 👉 계산이 아니라 그냥 텍스트
# 👉 반드시 변수 연산 필요

# ❌ [실수 6] 불필요한 슬라이싱
# num_list[:n]
# 👉 num_list와 동일 → 의미 없음

# ❌ [실수 7] list() 오용
# list(num_list + "문자열")
# 👉 문자열이 문자 단위로 분해됨 → 완전히 잘못된 결과


# 🔥 핵심 개념 정리

# 1. 마지막 원소 접근
# num_list[-1]

# 2. 이전 원소 접근
# num_list[-2]

# 3. 리스트 값 추가
# append(): 기존 리스트 수정
# + [값]: 새로운 리스트 생성

# 4. 계산은 문자열이 아니라 변수로
# last - secondLast (O)
# "last - secondLast" (X)