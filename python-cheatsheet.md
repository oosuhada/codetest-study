# 🧠 Python 코테 치트시트 (실전용 완전판)

---

# 🔥 1. 입력 / 출력

## 🔥 코테 최빈출 입력 문법 해부

```python
arr = list(map(int, input().split()))
```

이 한 줄이 코테에서 가장 많이 쓰이는 입력 패턴. 안에서 바깥 순서로 읽는다.

```python
# 1단계: input().split()
# "1 2 3 4 5" 입력 → ['1', '2', '3', '4', '5']  (문자열 리스트)
input().split()

# 2단계: map(int, ...)
# ['1', '2', '3'] → map 객체 (각 원소에 int 적용, 아직 리스트 아님)
map(int, ['1', '2', '3'])

# 3단계: list(...)
# map 객체 → [1, 2, 3]  (실제 리스트로 변환)
list(map(int, ...))
```

### 🔥 map() 핵심 패턴

```python
# map(함수, 반복가능객체) → 각 원소에 함수를 적용한 map 객체 반환
map(int, ['1', '2', '3'])      # 정수 변환
map(float, ['1.1', '2.2'])     # 실수 변환
map(str, [1, 2, 3])            # 문자열 변환
map(len, ['abc', 'de', 'f'])   # 각 원소의 길이

# list()로 감싸야 실제 리스트가 됨
list(map(int, ['1', '2']))     # [1, 2]
tuple(map(int, ['1', '2']))    # (1, 2)

# 언패킹으로 바로 변수에 받기 (두 수 입력)
a, b = map(int, input().split())

# 여러 개를 각각 다른 변수에
n, m, k = map(int, input().split())
```

### 🔥 split() 핵심 패턴

```python
"1 2 3".split()       # ['1', '2', '3']  기본: 공백
"1,2,3".split(',')    # ['1', '2', '3']  쉼표 기준
"abc".split()         # ['abc']          공백 없으면 통째로
"  1  2  ".split()    # ['1', '2']       양쪽 공백 자동 제거
```

### ❗ 자주 쓰는 입력 패턴 모음

```python
n = int(input())                              # 숫자 하나
a, b = map(int, input().split())              # 숫자 두 개
arr = list(map(int, input().split()))         # 숫자 여러 개 → 리스트
s = input()                                   # 문자열 그대로

# 2D 배열 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 문자열을 한 글자씩 리스트로
row = list(input())           # "101" → ['1', '0', '1']
row = list(map(int, input())) # "101" → [1, 0, 1]  ← 공백 없는 숫자열

# n줄 입력받기
data = [input() for _ in range(n)]
data = [list(map(int, input().split())) for _ in range(n)]
```

## 기타 입출력 패턴

```python
# 출력
print(n)
print(*arr)           # 리스트 공백 출력
print(*arr, sep=',')  # 쉼표로 출력

# 🔥 빠른 입력 (입력 많을 때 필수)
import sys
input = sys.stdin.readline
```

---

# 🔥 2. 반복문

```python
for i in range(n):           # 0 ~ n-1
for i in range(1, n+1):      # 1 ~ n
for i in range(n, 0, -1):    # n ~ 1 (역순)
for i in range(0, n, 2):     # 0, 2, 4 ... (step)

for num in arr:               # 리스트 순회
for i, v in enumerate(arr):  # 인덱스 + 값
for a, b in zip(arr1, arr2): # 두 개 동시에

# while
while n > 0:
    n -= 1
```

---

# 🔥 3. 조건문

```python
if n > 10:
    print("크다")
elif n == 10:
    print("같다")
else:
    print("작다")

# 비교 연산자
==  !=  >  <  >=  <=

# 논리 연산자
and   or   not

# 핵심 패턴
if num % n == 0:                       # 나눠떨어짐
if num % n == 0 and num % m == 0:      # 둘 다 나눠떨어짐
if a <= x <= b:                        # 범위 체크 (Python만 가능!)
```

## ❗ 자주 틀리는 것

```python
if flag == True:  ❌   →   if flag: ✅
if x = 10:        ❌   →   if x == 10: ✅
if x > 10         ❌   →   if x > 10: ✅ (콜론!)
```

---

# 🔥 4. 리스트

```python
arr = [1, 2, 3]
arr.append(4)          # 끝에 추가
arr.pop()              # 끝에서 제거
arr.pop(0)             # 앞에서 제거 (느림, 큐엔 deque 써라)
arr.insert(0, 99)      # 특정 위치 삽입
arr.remove(2)          # 값으로 제거 (첫 번째 하나만)
arr.index(3)           # 값의 인덱스 반환
arr.count(2)           # 개수 세기

arr.sort()             # 오름차순 정렬 (원본 변경)
arr.sort(reverse=True) # 내림차순
arr.reverse()          # 뒤집기 (원본 변경)

sorted(arr)            # 정렬된 새 리스트 반환 (원본 유지)

# 슬라이싱
arr[1:3]    # 인덱스 1~2
arr[:3]     # 처음~2
arr[2:]     # 2~끝
arr[::-1]   # 역순 복사

# 자주 쓰는 함수
max(arr)
min(arr)
sum(arr)
len(arr)
```

## 🔥 2차원 리스트

```python
# 초기화 (n행 m열)
graph = [[0] * m for _ in range(n)]   # ✅ 올바른 방법
graph = [[0] * m] * n                 # ❌ 행이 같은 객체를 참조함!

# 접근
graph[i][j]

# 순회
for row in graph:
    for val in row:
        print(val)

# 입력 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
```

---

# 🔥 5. 문자열

```python
s = "hello"
s.upper()
s.lower()
s.strip()          # 양쪽 공백 제거
s.split()          # 공백 기준 분리
s.split(',')       # 쉼표 기준 분리
s.replace("l","x") # 치환
s.find("e")        # 위치 반환 (-1이면 없음)
s.count("l")       # 개수

# 검사
s.isupper()  s.islower()  s.isalpha()  s.isdigit()  s.isalnum()

# 포함 여부
"abc" in "abcdef"   # True

# 🔥 합치기 (필수!)
''.join(arr)
' '.join(arr)

# 문자열 반복
"hi" * 3    # "hihihi"

# 형변환
str(a)      # 숫자 → 문자열
int("10")   # 문자열 → 숫자
list(s)     # 문자열 → 문자 리스트
```

## ❗ 비추천

```python
answer = ''
for a in arr:
    answer += a   # ❌ 느림! join 써라
```

---

# 🔥 6. 형변환

```python
str(a)
int("10")
float("3.14")
list("abc")    # ['a', 'b', 'c']
list(range(5)) # [0, 1, 2, 3, 4]
tuple(arr)
set(arr)
```

## 🔥 핵심 패턴

```python
int(str(a) + str(b))              # 두 숫자 이어붙이기
[int(x) for x in list(str(n))]   # 각 자릿수를 리스트로
```

---

# 🔥 7. 딕셔너리 (해시맵)

```python
d = {}
d["a"] = 1
d["b"] = 2
d.get("c", 0)         # 없으면 기본값 0
"a" in d              # 키 존재 여부

# 반복
for key in d:
    print(key)
for key, value in d.items():
    print(key, value)
for value in d.values():
    print(value)

# 🔥 카운트 패턴
from collections import defaultdict
d = defaultdict(int)   # 없는 키 접근해도 0으로 초기화
d["a"] += 1

from collections import Counter
cnt = Counter(arr)     # {값: 개수} 딕셔너리
cnt.most_common(3)     # 상위 3개 반환
```

---

# 🔥 8. 집합 (set)

```python
s = set()
s.add(1)
s.remove(1)
s.discard(1)   # 없어도 오류 안 남

# 집합 연산
a & b   # 교집합
a | b   # 합집합
a - b   # 차집합

# 중복 제거
arr = list(set(arr))   # ⚠️ 순서 보장 안 됨!
```

---

# 🔥 9. 스택 / 큐 (코테 필수!)

## 스택 (LIFO)

```python
stack = []
stack.append(1)   # push
stack.pop()       # pop (끝에서)

# 활용: 괄호 짝 맞추기, 뒤로가기
```

## 큐 (FIFO)

```python
from collections import deque

q = deque()
q.append(1)     # 오른쪽에 추가
q.popleft()     # 왼쪽에서 제거

# list.pop(0) 쓰지 마라 → O(n)으로 느림
# deque.popleft() → O(1)

# 활용: BFS, 순서대로 처리
```

---

# 🔥 10. 정렬

```python
arr.sort()                             # 오름차순
arr.sort(reverse=True)                 # 내림차순
arr.sort(key=len)                      # 길이 기준
arr.sort(key=lambda x: x[1])          # 두 번째 값 기준
arr.sort(key=lambda x: (x[1], x[0])) # 복합 기준

sorted(arr)                            # 원본 유지, 새 리스트 반환
sorted(arr, reverse=True)
sorted(arr, key=lambda x: -x)         # 내림차순 (음수 트릭)
```

---

# 🔥 11. 함수 / lambda

```python
def add(a, b):
    return a + b

# lambda: 간단한 함수
f = lambda x: x * 2
g = lambda x, y: x + y

# 조건 한 줄
return a + b if flag else a - b
```

---

# 🔥 12. 리스트 컴프리헨션

```python
[i for i in range(5)]
[i for i in range(10) if i % 2 == 0]
[i * 2 for i in arr if i > 0]

# 2차원
[[0] * m for _ in range(n)]
[[i * j for j in range(m)] for i in range(n)]
```

---

# 🔥 13. 완전탐색 (DFS/BFS) — 코테 핵심!

## BFS (너비 우선 탐색) — 최단 거리

```python
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
```

## DFS (깊이 우선 탐색) — 재귀

```python
def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
```

## 🔥 2D 그리드 탐색 (상하좌우)

```python
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
```

---

# 🔥 14. 재귀

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 🔥 재귀 깊이 늘리기 (필요 시)
import sys
sys.setrecursionlimit(10**6)
```

---

# 🔥 15. 이진 탐색

```python
# 직접 구현
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 라이브러리
from bisect import bisect_left, bisect_right
arr = sorted(arr)
bisect_left(arr, x)   # x 이상인 첫 위치
bisect_right(arr, x)  # x 초과인 첫 위치
```

---

# 🔥 16. 우선순위 큐 (힙)

```python
import heapq

# 최소 힙 (기본)
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappop(heap)   # 가장 작은 값 꺼냄

# 최대 힙 (음수로 저장)
heapq.heappush(heap, -3)
-heapq.heappop(heap)  # 가장 큰 값

# 리스트를 힙으로
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)
```

---

# 🔥 17. 순열 / 조합

```python
from itertools import permutations, combinations, product

# 순열 (순서 있음)
list(permutations([1, 2, 3], 2))   # [(1,2),(1,3),(2,1)...]

# 조합 (순서 없음)
list(combinations([1, 2, 3], 2))   # [(1,2),(1,3),(2,3)]

# 중복 조합
from itertools import combinations_with_replacement
list(combinations_with_replacement([1,2,3], 2))

# 데카르트 곱 (중복 순열)
list(product([1,2], repeat=3))   # 2^3 = 8가지
```

---

# 🔥 18. 유용한 내장 함수

```python
abs(-10)                         # 절댓값
round(3.14)                      # 반올림
pow(2, 10)                       # 2^10 (= 2**10)
divmod(7, 3)                     # (2, 1) → 몫, 나머지
any([False, True, False])        # 하나라도 True면 True
all([True, True, True])          # 모두 True여야 True
```

---

# 🔥 19. 난수 (random)

```python
import random

random.random()               # 0.0 이상 1.0 미만 float 난수
random.randint(1, 10)         # 1 이상 10 이하 int 난수 (양 끝 포함!)
random.randrange(0, 10)       # 0 이상 10 미만 int 난수 (range처럼)
random.choice([1, 2, 3])      # 리스트에서 랜덤 요소 1개 선택
random.choices([1,2,3], k=2)  # 중복 허용, k개 선택
random.sample([1,2,3,4], 2)   # 중복 없이 k개 선택
random.shuffle(arr)           # 리스트 제자리에서 섞기 (반환값 없음!)
```

## ❗ 자주 틀리는 것

```python
arr = random.shuffle(arr)   # ❌ None 반환됨!
random.shuffle(arr)         # ✅ 원본을 직접 수정

random.randint(1, 10)       # ✅ 10 포함
random.randrange(1, 10)     # ⚠️ 10 미포함 (range와 동일)
```

---

# 🔥 20. 날짜와 시간 (datetime)

```python
from datetime import datetime, date, timedelta

# 현재 날짜/시간
now = datetime.now()         # 날짜 + 시간
today = date.today()         # 날짜만

# 값 가져오기
now.year
now.month                    # 1 ~ 12 (1월 = 1)
now.day
now.hour
now.minute
now.second
now.weekday()                # 월=0 ~ 일=6
now.isoweekday()             # 월=1 ~ 일=7

# 특정 날짜 생성
d = date(2024, 1, 1)
dt = datetime(2024, 1, 1, 9, 30, 0)

# 날짜 연산 (timedelta)
d + timedelta(days=7)        # 7일 후
d - timedelta(weeks=1)       # 1주 전
dt + timedelta(hours=3)      # 3시간 후

# 날짜 차이
diff = d2 - d1               # timedelta 객체
diff.days                    # 일수 차이 (정수)
diff.total_seconds()         # 초 단위 차이

# 비교
d1 < d2
d1 == d2

# 포맷
now.strftime("%Y-%m-%d %H:%M:%S")            # datetime → 문자열
datetime.strptime("2024-01-01", "%Y-%m-%d")  # 문자열 → datetime
```

## 🔥 자주 쓰는 포맷 코드

```plaintext
%Y  연도 (2024)
%m  월 (01~12)
%d  일 (01~31)
%H  시 (00~23)
%M  분 (00~59)
%S  초 (00~59)
%A  요일 영문 (Monday...)
%j  연중 몇 번째 날 (001~366)
```

## ❗ 자주 틀리는 것

```python
diff = d2 - d1
diff               # timedelta(days=364)
diff.days          # ✅ 364  ← 이걸 써야 숫자로 쓸 수 있음
int(diff)          # ❌ 에러!

# weekday vs isoweekday
now.weekday()      # 월=0, 일=6
now.isoweekday()   # 월=1, 일=7  ← 헷갈리면 이거 써라
```

---

# 🔥 21. 핵심 패턴 모음

## 문자열 번갈아 합치기

```python
result = []
for a, b in zip(str1, str2):
    result.append(a)
    result.append(b)
return ''.join(result)
```

## 숫자를 자릿수 리스트로

```python
digits = [int(d) for d in str(n)]
```

## 최댓값 인덱스

```python
idx = arr.index(max(arr))
```

## 리스트 초기화

```python
[0] * 5                      # [0, 0, 0, 0, 0]
[[0]*m for _ in range(n)]    # 2D
```

## 딕셔너리 카운트

```python
d = {}
for x in arr:
    d[x] = d.get(x, 0) + 1
```

## unpacking

```python
a, b = 1, 2
a, b = b, a                  # 🔥 스왑
a, b = [1, 2]
a, *rest = [1, 2, 3, 4]      # a=1, rest=[2,3,4]
```

---

# 🔥 22. 실수 체크리스트

```plaintext
1.  : 붙였는가?
2.  == 썼는가? (= 아니라)
3.  True/False 대문자인가?
4.  인덱스 범위 초과 안 했는가?
5.  join 대신 += 안 썼는가?
6.  IndexError 가능성 체크
7.  문자열 + 숫자 ❌ (str() 변환)
8.  join 안에 숫자 ❌ (str 변환 후)
9.  2D 배열 [[0]*m]*n ❌ (같은 행 공유!)
10. sort()는 원본 변경, sorted()는 새 리스트
11. deque 대신 list.pop(0) 쓰면 느림
12. 재귀 깊이 기본 1000 → setrecursionlimit 필요 시
13. random.shuffle() 반환값 없음 → 원본 직접 수정됨
14. timedelta 차이는 .days로 꺼내야 숫자로 사용 가능
```

---

# 🚀 핵심 무기 요약

| 상황 | 사용 |
|---|---|
| 문자열 합치기 | `join` |
| 두 리스트 동시 | `zip` |
| 인덱스 필요 | `enumerate` |
| 정렬 | `sort` / `sorted` |
| 카운트 | `Counter` |
| 중복 제거 | `set` |
| BFS | `deque` |
| 최솟값/최댓값 빠르게 | `heapq` |
| 완전탐색 | 순열/조합 `itertools` |
| 이진탐색 | `bisect` |
| 난수 | `random.randint` / `random.choice` |
| 날짜/시간 | `datetime` / `timedelta` |

---

# 🔥 최종 한 줄

👉 "문법은 외우는 게 아니라 반복해서 자동화한다 — 패턴이 보이면 코드가 나온다"