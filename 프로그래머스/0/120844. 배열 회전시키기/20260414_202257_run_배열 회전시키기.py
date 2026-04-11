# ============================================================
# 오류 원인 분석
# ============================================================

# [오류 1] 빈 배열에 인덱스로 값을 넣으려 했다
#
#   answer = []         ← 크기가 0인 빈 배열
#   answer[0] = 무언가  ← 0번 자리가 없음 → IndexError!
#
#   파이썬 리스트는 C나 Java의 배열과 다르게
#   "미리 크기를 잡아두는" 개념이 없다.
#   빈 리스트에 answer[0] = x 는 불가능하고,
#   answer.append(x) 로 뒤에 추가하거나
#   answer = [0] * n   처럼 미리 크기를 만들어야 한다.

# [오류 2] for문과 while문을 잘못 중첩했다
#
#   for i in numbers[i]:  ← numbers[i]는 정수 하나 (예: 1)
#                            정수를 for로 순회할 수 없다 → TypeError
#   while i < n:
#       for i in numbers[i]:  ← 같은 i를 while과 for가 동시에 쓰고 있음
#                                서로 i를 덮어써서 무한루프나 오류 발생
#
#   인덱스로 순회할 때는 for + range를 쓰는 게 맞다
#   for i in range(n):  ← i = 0, 1, 2, ... n-1


# ============================================================
# 기존 코드 수정 완성 (append 방식)
# ============================================================

def solution_v1(numbers, direction):
    answer = []
    n = len(numbers)

    if direction == "right":
        answer.append(numbers[n-1])   # 마지막 원소를 맨 앞에
        for i in range(n-1):          # 나머지를 순서대로 뒤에
            answer.append(numbers[i])

    elif direction == "left":
        for i in range(1, n):         # 1번 인덱스부터 끝까지 먼저
            answer.append(numbers[i])
        answer.append(numbers[0])     # 첫 원소를 맨 뒤에

    return answer


# ============================================================
# 기존 코드 수정 완성 (미리 크기 잡는 방식)
# ============================================================

def solution_v2(numbers, direction):
    n = len(numbers)
    answer = [0] * n   # 크기 n짜리 배열을 0으로 미리 만들어 둠
                       # → 이제 answer[0], answer[n-1] 등 인덱스 접근 가능

    if direction == "right":
        answer[0] = numbers[n-1]      # 마지막 원소 → 맨 앞
        for i in range(n-1):          # 나머지를 한 칸씩 오른쪽으로
            answer[i+1] = numbers[i]

    elif direction == "left":
        answer[n-1] = numbers[0]      # 첫 원소 → 맨 뒤
        for i in range(1, n):         # 나머지를 한 칸씩 왼쪽으로
            answer[i-1] = numbers[i]

    return answer


# ============================================================
# 깔끔한 풀이 (파이썬 슬라이싱 활용)
# ============================================================

def solution(numbers, direction):
    # 파이썬 리스트 슬라이싱으로 한 줄에 해결
    # numbers[-1:]     → 마지막 원소 1개를 리스트로
    # numbers[:-1]     → 마지막 원소 빼고 앞부분
    # numbers[1:]      → 첫 원소 빼고 뒷부분
    # numbers[:1]      → 첫 원소 1개를 리스트로

    if direction == "right":
        return numbers[-1:] + numbers[:-1]
        # [3] + [1, 2]  →  [3, 1, 2]

    elif direction == "left":
        return numbers[1:] + numbers[:1]
        # [2, 3] + [1]  →  [2, 3, 1]
