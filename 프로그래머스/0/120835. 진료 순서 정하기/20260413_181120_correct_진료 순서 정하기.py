# ============================================================
# 문제: 진료 순서 정하기
# 각 원소에 대해 "나보다 큰 수가 몇 개인가 + 1" = 순위
# ============================================================

def solution(emergency):
    answer = []
    for x in emergency:
        rank = sum(1 for e in emergency if e > x) + 1
        answer.append(rank)
    return answer

# rank = sum(1 for e in emergency if e > x) + 1 의 풀이

# count = 0
# for e in emergency:
#     if e > x:
#         count += 1   # 나보다 큰 수를 발견할 때마다 1씩 누적
# rank = count + 1     # 나보다 큰 수가 count개 → 나는 count+1등

# 풀이 B — sorted()로 순위표 만들기 (내가 시도하던 방향과 가장 가까움)
# ----------------------------------------------------------
# 내가 시도했던 흐름:
#   "큰 숫자부터 1, 2, 3 순서로 치환하기"
#   → 이 아이디어를 sorted()로 구현할 수 있음!
#
# 핵심 아이디어:
#   1) emergency를 내림차순으로 정렬 → 그 순서가 곧 순위
#   2) 각 원소가 정렬된 배열의 몇 번째 위치인지 찾으면 됨
#
# 예) emergency = [3, 76, 24]
#     sorted_desc = [76, 24, 3]
#     76의 위치 = index 0 → 0+1 = 1등
#     24의 위치 = index 1 → 1+1 = 2등
#      3의 위치 = index 2 → 2+1 = 3등
 
def solution_B(emergency):
    sorted_desc = sorted(emergency, reverse=True)  # 내림차순 정렬
    answer = []
    for x in emergency:
        rank = sorted_desc.index(x) + 1  # 정렬된 배열에서 내 위치 + 1
        answer.append(rank)
    return answer
 
 
# 풀이 C — 딕셔너리로 순위표 만들기 (풀이 B의 업그레이드)
# ----------------------------------------------------------
# 풀이 B에서 .index()는 매번 배열을 처음부터 탐색함
# 딕셔너리를 쓰면 순위를 미리 {숫자: 순위} 형태로 저장해놓고
# 바로 꺼내 쓸 수 있어서 더 깔끔함
#
# 예) rank_map = {76: 1, 24: 2, 3: 3}
#     emergency = [3, 76, 24]
#     → [rank_map[3], rank_map[76], rank_map[24]]
#     → [3, 1, 2]
 
def solution_C(emergency):
    sorted_desc = sorted(emergency, reverse=True)
    rank_map = {}
    for i, val in enumerate(sorted_desc):  # i=0,1,2... val=76,24,3...
        rank_map[val] = i + 1              # {76:1, 24:2, 3:3}
 
    answer = []
    for x in emergency:
        answer.append(rank_map[x])
    return answer

# ============================================================
# 오답노트
# ============================================================

#     #배열 안에서 큰 숫자부터 1, 2, 3 순서대로 치환하기
#     n = len(emergency) #[1부터 n까지 배열]을 숫자 순서대로 치환
#     index = list(range(1:n+1))
#     #1th, 2nd, 3rd 이런식으로 치환하는 방법이 array 말고 있을까?
#     #array(emergency)로 순서를 바꿔버리면 다시 원래대로 돌릴 수 있는 방법이 없지 않나?
    
#     while i < n+2:
#         for c in emergency:
#             max(c).replace('i')
#             i += 1 

# ❌ 내가 쓴 틀린 코드
# ----------------------------------------------------------
# def solution(emergency):
#     n = len(emergency)
#     index = list(range(1:n+1))       # 오류 1
#
#     while i < n+2:                   # 오류 3
#         for c in emergency:
#             max(c).replace('i')      # 오류 2
#             i += 1
#     return emergency


# 🔴 오류 1: range(1:n+1) — 슬라이싱과 range 혼동
# ----------------------------------------------------------
# index = list(range(1:n+1))   # ❌ SyntaxError
# index = list(range(1, n+1))  # ✅
#
# - range(start, stop) 의 인자는 콤마(,)로 구분
# - list[1:n+1] 처럼 콜론(:)은 슬라이싱 전용 문법
# - 둘을 섞으면 SyntaxError 발생


# 🔴 오류 2: max(c).replace('i') — max와 replace 오용
# ----------------------------------------------------------
# (1) max() 오용
# - for c in emergency 에서 c는 이미 단일 정수
# - max(c) 처럼 정수 하나를 넣는 건 의미 없음
# - 배열의 최댓값을 구하려면 max(emergency) 처럼 배열 전체를 인자로 넘겨야 함
#
# (2) replace() 오용
# - replace()는 str(문자열) 전용 메서드 → 정수에 쓰면 AttributeError
# - 배열의 값을 바꾸고 싶으면 인덱스로 직접 재할당해야 함
#   예: emergency[0] = 1


# 🔴 오류 3: while i < n+2 — i 미정의 & 루프 구조 혼동
# ----------------------------------------------------------
# - i를 한 번도 선언하지 않고 while 조건에 사용 → NameError
#   while을 쓰려면 앞에서 반드시 i = 0 같이 초기화 필요
# - while + for 중첩은 이 문제에서 불필요한 구조
# - 순위를 매기는 작업은 for 반복문 하나로 충분
# - 원본 배열을 직접 수정하면 인덱스(원래 위치 정보)가 사라짐
#   → 결과는 새 배열 answer = [] 에 따로 담아야 함


# ✅ 핵심 아이디어
# ----------------------------------------------------------
# emergency = [30, 10, 23, 6, 100]
#
# 각 원소에 대해: "나보다 큰 수가 몇 개?" + 1 = 내 순위
#
# 원소   나보다 큰 수 개수   순위
#  30       1개 (100)        2
#  10       3개              4
#  23       2개              3
#   6       4개              5
# 100       0개              1
#
# → result = [2, 4, 3, 5, 1]
