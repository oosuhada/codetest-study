# =========================================================
# 📌 최빈값 구하기 - 오답노트 (완전 정리)
# =========================================================


# =========================================================
# 1. ❌ 내가 작성한 코드의 문제점
# =========================================================

# def solution(array):
#     counts = array.count(i) for i in array()
#     max_counts = counts.max 
#     
#     if counts.max > 1:
#         return -1
#     else:
#         return i
#     
#     return array[i]


# ❗ 문제 분석

# (1) 리스트 컴프리헨션 문법 오류
# counts = array.count(i) for i in array()
# → 반드시 [] 필요
# → 그리고 array() ❌ (리스트는 함수가 아님)

# (2) counts 자료형 문제
# counts는 리스트여야 하는데 현재는 문법 자체가 깨짐

# (3) max 사용법 틀림
# counts.max ❌
# → max(counts) ⭕

# (4) 조건식 완전 틀림
# if counts.max > 1:
# → "최빈값이 여러 개"를 판단하는 조건이 아님

# (5) i 사용 위치 오류
# → for문 밖에서 i는 의미 없음

# (6) return array[i]
# → i가 뭔지도 불명확 + 인덱스 로직 자체가 틀림


# =========================================================
# 2. ✅ 실수 수정 버전 (네 접근 최대 유지)
# =========================================================

def solution(array):
    values = list(set(array))  # 중복 제거 (등장한 값만)
    counts = [array.count(i) for i in values]

    max_count = max(counts)

    # 최댓값이 몇 개인지 확인
    if counts.count(max_count) > 1:
        return -1
    else:
        return values[counts.index(max_count)]


# =========================================================
# 3. 🚀 개선된 추천 스타일 (코테 정석)
# =========================================================

from collections import Counter

def solution(array):
    counter = Counter(array)
    max_count = max(counter.values())

    modes = [k for k, v in counter.items() if v == max_count]

    if len(modes) > 1:
        return -1
    return modes[0]


# =========================================================
# 4. ⚠️ 내가 틀리기 쉬운 부분 정리
# =========================================================

# 🔥 리스트 vs 함수 구분
# array() ❌ / array ⭕

# 🔥 리스트 컴프리헨션 문법
# [array.count(i) for i in array] ⭕

# 🔥 max 사용법
# counts.max ❌ / max(counts) ⭕

# 🔥 "최빈값 여러 개" 판단 방법
# → max가 2 이상이 아니라
# → max값을 가진 요소의 개수를 세야 함

# 🔥 변수 i 스코프
# → for문 밖에서는 의미 없음

# 🔥 값 vs 인덱스 혼동
# → counts.index(max_count)는 "위치"
# → 실제 값은 따로 매핑 필요


# =========================================================
# 5. 🧠 핵심 개념 정리
# =========================================================

# ✔ 최빈값 문제의 본질
# → "값" 문제가 아니라 "빈도 비교" 문제

# ✔ 해결 구조
# 1. 값 → 등장 횟수 매핑 만들기
# 2. 최대 등장 횟수 찾기
# 3. 그 횟수를 가진 값이 몇 개인지 확인
#    - 1개 → 반환
#    - 여러 개 → -1

# ✔ 핵심 공식
# max_count = max(빈도들)
# 빈도들.count(max_count)


# =========================================================
# 6. 🧪 테스트
# =========================================================

# if __name__ == "__main__":
#     print(solution_best([1, 2, 3, 3, 3, 4]))  # 3
#     print(solution_best([1, 1, 2, 2]))        # -1
#     print(solution_best([1]))                # 1