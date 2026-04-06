# 🧠 Python 코테 치트시트 (실전용 완전판)

---

# 🔥 0. print 출력 완전 정복

코테에서 출력 형식이 틀리면 무조건 오답. 제일 먼저 마스터해야 한다.

## 0-1. 따옴표 — ', ", ''' 차이

```python
# 작은따옴표 / 큰따옴표 → 동일하게 문자열 만들기
print('hello')      # hello
print("hello")      # hello

# ⭐ 문자열 안에 따옴표를 넣어야 할 때
print("I'm fine")          # 큰따옴표 안에 작은따옴표 → OK
print('He said "hi"')      # 작은따옴표 안에 큰따옴표 → OK

# 같은 따옴표가 충돌하면 → 백슬래시(\)로 탈출
print('I\'m fine')         # 작은따옴표 안에 작은따옴표 → \' 로 탈출
print("He said \"hi\"")    # 큰따옴표 안에 큰따옴표 → \" 로 탈출

# 삼중따옴표 → 여러 줄 문자열, 따옴표 혼용 가능
print("""첫째 줄
둘째 줄
셋째 줄""")
```

## 0-2. 특수문자 출력 — 백슬래시(\) 탈출 규칙

```python
# \n  → 줄바꿈
# \t  → 탭
# \\  → 백슬래시 자체 출력
# \'  → 작은따옴표
# \"  → 큰따옴표

print("줄1\n줄2")     # 줄1
                      # 줄2
print("a\tb")         # a   b  (탭 간격)
print("C:\\Users")    # C:\Users

# 🔥 실전 예시: !@#$%^&*(\'"<>?:; 출력
# ' 와 " 가 섞여 있어서 한 종류 따옴표로는 불가능

# 방법1: 서로 다른 따옴표 + 이어붙이기
print('!@#$%^&*(\\' + '\'"<>?:;')

# 방법2: 백슬래시로 전부 탈출
print('!@#$%^&*(\\\'\"<>?:;')

# 방법3 (가장 안전): 삼중따옴표
print("""!@#$%^&*(\'"<>?:;""")
```

## 0-3. print 콤마(,) vs f-string vs + 연산

```python
a, b = 4, 5

# ✅ 콤마(,) 방식 — 코테에서 가장 빠르고 안전
print(a, "+", b, "=", a + b)    # 4 + 5 = 9
# 자동으로 str 변환, 사이에 공백 삽입
# sep 옵션으로 구분자 변경 가능
print(a, b, sep=",")            # 4,5
print(a, b, sep="")             # 45

# ✅ f-string — 가독성 최고, 실무/코테 모두 사용
print(f"{a} + {b} = {a + b}")  # 4 + 5 = 9
print(f"{a:.2f}")               # 4.00  (소수점 포맷)
print(f"{a:05d}")               # 00004 (0 패딩)

# ❌ + 연산 — 숫자는 반드시 str() 변환 필요
print("a = " + str(a))         # ✅
print("a = " + a)              # ❌ TypeError!

# end 옵션 — 기본값은 '\n' (줄바꿈)
print("hello", end=" ")        # 줄바꿈 없이 공백으로 끝냄
print("world")                 # → hello world (한 줄)
```

## 0-4. 출력 패턴 모음

```python
# 리스트 내용 공백으로 출력
arr = [1, 2, 3]
print(*arr)                    # 1 2 3  (언패킹)
print(*arr, sep=",")           # 1,2,3

# 여러 줄 출력
for x in arr:
    print(x)

# 숫자 포맷
print(f"{3.14159:.2f}")        # 3.14
print(f"{42:05d}")             # 00042
print(f"{1000000:,}")          # 1,000,000
```

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

# 언패킹으로 바로 변수에 받기
a, b = map(int, input().split())
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
n = int(input())                               # 숫자 하나
a, b = map(int, input().split())               # 숫자 두 개
arr = list(map(int, input().split()))          # 숫자 여러 개 → 리스트
s = input()                                    # 문자열 그대로

# 2D 배열 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 문자열을 한 글자씩 리스트로
row = list(input())            # "101" → ['1', '0', '1']
row = list(map(int, input()))  # "101" → [1, 0, 1]  ← 공백 없는 숫자열

# n줄 입력받기
data = [input() for _ in range(n)]
data = [list(map(int, input().split())) for _ in range(n)]

# 🔥 빠른 입력 (입력 많을 때 필수)
import sys
input = sys.stdin.readline
# ⚠️ readline은 줄 끝 \n 포함 → strip() 붙이는 게 안전
s = input().strip()
```

---

# 🔥 2. 문자열 완전 정복

## 2-1. 기본 메서드

```python
s = "Hello World"
s.upper()               # "HELLO WORLD"
s.lower()               # "hello world"
s.swapcase()            # 대소문자 교체 "hELLO wORLD"
s.strip()               # 양쪽 공백 제거
s.lstrip()              # 왼쪽 공백 제거
s.rstrip()              # 오른쪽 공백 제거
s.replace("l", "x")    # "Hexxo Worxd"
s.find("o")             # 4  (첫 번째 위치, 없으면 -1)
s.index("o")            # 4  (없으면 ValueError!)
s.count("l")            # 3
s.split()               # ['Hello', 'World']
s.split("o")            # ['Hell', ' W', 'rld']
' '.join(['a','b','c']) # "a b c"

# 검사
s.isupper()             # 모두 대문자?
s.islower()             # 모두 소문자?
s.isalpha()             # 모두 알파벳?
s.isdigit()             # 모두 숫자?
s.isalnum()             # 알파벳 또는 숫자?
s.startswith("He")      # True
s.endswith("ld")        # True

# 포함 여부
"abc" in "abcdef"       # True
"xyz" not in "abc"      # True
```

## 2-2. 메서드 모를 때 → 조건문으로 직접 구현

```python
# 🔥 swapcase() 모를 때 → isupper/islower로 직접
s = "Hello"
result = ""
for c in s:
    if c.isupper():
        result += c.lower()
    else:
        result += c.upper()
print(result)   # "hELLO"

# 🔥 isdigit() 대신 범위 조건으로
for c in s:
    if '0' <= c <= '9':     # 아스키 범위로 숫자 판별
        print(f"{c}는 숫자")

# 🔥 upper() 대신 아스키 코드로
for c in s:
    if 'a' <= c <= 'z':     # 소문자면
        print(chr(ord(c) - 32))  # 대문자로 변환
```

## 2-3. 아스키 코드 (ord / chr)

```python
ord('a')    # 97
ord('A')    # 65
ord('0')    # 48

chr(97)     # 'a'
chr(65)     # 'A'

# 🔥 실전 패턴
ord('c') - ord('a')    # 2  (알파벳 순서 인덱스)
chr(ord('a') + 3)      # 'd'  (3번째 뒤 알파벳)

# 대소문자 차이는 항상 32
ord('a') - ord('A')    # 32
# 소문자 → 대문자: ord(c) - 32
# 대문자 → 소문자: ord(c) + 32
```

## 2-4. 문자열 슬라이싱 — 코테 단골

```python
s = "abcdef"

s[0]        # 'a'  (첫 번째)
s[-1]       # 'f'  (마지막)
s[1:4]      # 'bcd'  (1 이상 4 미만)
s[:3]       # 'abc'  (처음~2)
s[3:]       # 'def'  (3~끝)
s[::-1]     # 'fedcba'  (역순)
s[::2]      # 'ace'  (2 step)

# 🔥 문자열은 immutable → 직접 수정 불가 → 잘라서 붙이기

# 삽입: str[:i] + new + str[i:]
result = s[:3] + "ZZZ" + s[3:]    # "abcZZZdef"

# 교체: str[:i] + replace + str[i+len(replace):]
replace = "ZZ"
i = 2
result = s[:i] + replace + s[i+len(replace):]   # "abZZef"

# 삭제: str[:i] + str[i+k:]
i, k = 2, 3
result = s[:i] + s[i+k:]          # "abf"

# 한 글자 교체 (인덱스 i의 문자를 'X'로)
i = 2
result = s[:i] + 'X' + s[i+1:]   # "abXdef"
```

## 2-5. 자주 쓰는 문자열 패턴

```python
# 문자열 뒤집기
s[::-1]
''.join(reversed(s))

# 팰린드롬 확인
s == s[::-1]

# 문자 반복 출력
print("hi" * 3)     # hihihi

# 문자열을 세로로 출력 (90도 회전 효과)
for c in s:
    print(c)

# 공백 없는 숫자열 → 각 자리 정수 리스트
digits = list(map(int, input()))   # "12345" → [1,2,3,4,5]

# 특정 문자 제거
s.replace("a", "")

# 특정 종류 문자만 남기기
result = ''.join(c for c in s if c.isalpha())
```

---

# 🔥 3. 반복문

```python
for i in range(n):           # 0 ~ n-1
for i in range(1, n+1):      # 1 ~ n
for i in range(n, 0, -1):    # n ~ 1 (역순)
for i in range(0, n, 2):     # 0, 2, 4 ... (step)

for num in arr:               # 리스트 순회
for i, v in enumerate(arr):  # 인덱스 + 값
for a, b in zip(arr1, arr2): # 두 리스트 동시에

# while
while n > 0:
    n -= 1

# break / continue
for i in range(10):
    if i == 5:
        break       # 반복 종료
    if i % 2 == 0:
        continue    # 이번 회차 건너뜀

# for-else (break 없이 끝났을 때만 else 실행)
for i in range(n):
    if arr[i] == target:
        print("찾음")
        break
else:
    print("없음")
```

---

# 🔥 4. 조건문

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
if num % 2 == 0:                       # 짝수
if num % n == 0:                       # n의 배수
if num % n == 0 and num % m == 0:      # n과 m 둘 다 배수
if a <= x <= b:                        # 범위 체크 (Python만 가능!)
if not arr:                            # 리스트가 비었으면
if arr:                                # 리스트가 비지 않았으면

# 삼항 연산자 (한 줄 조건)
result = "짝수" if n % 2 == 0 else "홀수"
print(f"{n} is even" if n % 2 == 0 else f"{n} is odd")
```

## ❗ 자주 틀리는 것

```python
if flag == True:  ❌   →   if flag: ✅
if x = 10:        ❌   →   if x == 10: ✅
if x > 10         ❌   →   if x > 10: ✅ (콜론!)
```

---

# 🔥 5. 리스트

```python
arr = [1, 2, 3]
arr.append(4)          # 끝에 추가
arr.pop()              # 끝에서 제거 (반환값 있음)
arr.pop(0)             # 앞에서 제거 (느림! 큐엔 deque 써라)
arr.insert(0, 99)      # 특정 위치 삽입
arr.remove(2)          # 값으로 제거 (첫 번째 하나만, 없으면 ValueError)
arr.index(3)           # 값의 인덱스 반환 (없으면 ValueError)
arr.count(2)           # 개수 세기
arr.extend([4,5])      # 다른 리스트 이어붙이기 (append와 다름!)

arr.sort()             # 오름차순 정렬 (원본 변경, 반환값 None)
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
graph = [list(map(int, input().split())) for _ in range(n)]
```

## ❗ append vs extend

```python
arr = [1, 2, 3]
arr.append([4, 5])    # [1, 2, 3, [4, 5]]  ← 리스트가 원소로 들어감
arr.extend([4, 5])    # [1, 2, 3, 4, 5]    ← 원소들이 풀려서 들어감
```

---

# 🔥 6. 형변환

```python
str(123)          # "123"
int("10")         # 10
int("10", 2)      # 2   (2진수 문자열 → 10진수)
int("ff", 16)     # 255 (16진수 문자열 → 10진수)
float("3.14")     # 3.14
list("abc")       # ['a', 'b', 'c']
list(range(5))    # [0, 1, 2, 3, 4]
tuple(arr)
set(arr)
```

## 🔥 핵심 패턴

```python
int(str(a) + str(b))              # 두 숫자 이어붙이기: 12, 34 → 1234
[int(x) for x in list(str(n))]   # 각 자릿수를 리스트로: 123 → [1,2,3]
bin(10)                           # '0b1010'  (2진수 문자열)
hex(255)                          # '0xff'    (16진수 문자열)
bin(10)[2:]                       # '1010'    (접두사 제거)
```

---

# 🔥 7. 딕셔너리 (해시맵)

```python
d = {}
d["a"] = 1
d["b"] = 2
d.get("c", 0)         # 없으면 기본값 0 (KeyError 안 남)
d["c"]                # 없으면 KeyError!
"a" in d              # 키 존재 여부
del d["a"]            # 키 삭제

# 반복
for key in d:
    print(key)
for key, value in d.items():
    print(key, value)
for value in d.values():
    print(value)
for key in sorted(d):           # 키 정렬 후 순회
    print(key, d[key])

# 🔥 카운트 패턴 1 — get으로 직접
d = {}
for x in arr:
    d[x] = d.get(x, 0) + 1

# 🔥 카운트 패턴 2 — defaultdict
from collections import defaultdict
d = defaultdict(int)    # 없는 키 접근 → 0으로 자동 초기화
d["a"] += 1

# 🔥 카운트 패턴 3 — Counter (가장 간단)
from collections import Counter
cnt = Counter(arr)      # {값: 개수} 딕셔너리
cnt.most_common(3)      # 상위 3개 [(값, 개수), ...]
cnt["x"]               # 없어도 0 반환 (KeyError 안 남)
```

---

# 🔥 8. 집합 (set)

```python
s = set()
s = {1, 2, 3}
s.add(4)
s.remove(1)        # 없으면 KeyError
s.discard(1)       # 없어도 오류 안 남
len(s)
x in s             # O(1) ← 리스트보다 훨씬 빠름!

# 집합 연산
a & b   # 교집합
a | b   # 합집합
a - b   # 차집합
a ^ b   # 대칭 차집합 (한쪽에만 있는 것)

# 중복 제거
arr = list(set(arr))   # ⚠️ 순서 보장 안 됨!
```

---

# 🔥 9. 스택 / 큐 (코테 필수!)

## 스택 (LIFO)

```python
stack = []
stack.append(1)    # push
stack.pop()        # pop (끝에서, 비어있으면 IndexError)
stack[-1]          # top 확인 (제거 안 함)
if stack:          # 비었는지 확인

# 활용: 괄호 짝 맞추기, 뒤로가기, 단조 스택
# 🔥 괄호 짝 맞추기 패턴
stack = []
for c in s:
    if c == '(':
        stack.append(c)
    elif c == ')':
        if not stack:
            print("불일치")
            break
        stack.pop()
```

## 큐 (FIFO)

```python
from collections import deque

q = deque()
q.append(1)        # 오른쪽에 추가
q.popleft()        # 왼쪽에서 제거 → O(1)
q.appendleft(1)    # 왼쪽에 추가
q.pop()            # 오른쪽에서 제거

# list.pop(0) 쓰지 마라 → O(n)으로 느림
# deque.popleft() → O(1)

# 활용: BFS, 순서대로 처리
```

---

# 🔥 10. 정렬

```python
arr.sort()                              # 오름차순 (원본 변경, 반환 None)
arr.sort(reverse=True)                  # 내림차순
arr.sort(key=len)                       # 길이 기준
arr.sort(key=lambda x: x[1])           # 두 번째 값 기준
arr.sort(key=lambda x: (x[1], x[0]))   # 복합 기준 (x[1] 우선, 같으면 x[0])
arr.sort(key=lambda x: (-x[1], x[0]))  # x[1] 내림차순, x[0] 오름차순

sorted(arr)                             # 원본 유지, 새 리스트 반환
sorted(arr, reverse=True)
sorted(arr, key=lambda x: -x)          # 내림차순 (음수 트릭)

# 문자열 정렬
words.sort()                            # 알파벳 순
words.sort(key=len)                     # 길이 순
words.sort(key=lambda x: (len(x), x))  # 길이 우선, 같으면 사전순
```

---

# 🔥 11. 함수

```python
def add(a, b):
    return a + b

# 기본값 인자
def greet(name, msg="Hello"):
    return f"{msg}, {name}"

# 여러 값 반환
def minmax(arr):
    return min(arr), max(arr)

mn, mx = minmax([1, 2, 3])

# lambda: 간단한 함수
f = lambda x: x * 2
g = lambda x, y: x + y

# 삼항 조건
return a + b if flag else a - b
```

---

# 🔥 12. 리스트 컴프리헨션

```python
[i for i in range(5)]
[i for i in range(10) if i % 2 == 0]
[i * 2 for i in arr if i > 0]
[c.upper() for c in s if c.isalpha()]    # 문자열 처리

# 2차원
[[0] * m for _ in range(n)]
[[i * j for j in range(m)] for i in range(n)]

# 조건부 값 (삼항)
[x if x > 0 else 0 for x in arr]        # 음수는 0으로
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
    if n <= 1:      # 🔥 base case 반드시 필요
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
bisect_left(arr, x)    # x 이상인 첫 위치
bisect_right(arr, x)   # x 초과인 첫 위치

# 특정 값의 개수
cnt = bisect_right(arr, x) - bisect_left(arr, x)
```

---

# 🔥 16. 우선순위 큐 (힙)

```python
import heapq

# 최소 힙 (기본)
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappop(heap)    # 가장 작은 값 꺼냄
heap[0]                # 최솟값 확인 (꺼내지 않음)

# 최대 힙 (음수로 저장)
heapq.heappush(heap, -3)
-heapq.heappop(heap)   # 가장 큰 값

# (우선순위, 값) 튜플 사용
heapq.heappush(heap, (2, "b"))
heapq.heappush(heap, (1, "a"))
priority, val = heapq.heappop(heap)   # (1, "a")

# 리스트를 힙으로
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)
```

---

# 🔥 17. 순열 / 조합

```python
from itertools import permutations, combinations, product

# 순열 (순서 있음)
list(permutations([1, 2, 3], 2))   # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# 조합 (순서 없음)
list(combinations([1, 2, 3], 2))   # [(1,2),(1,3),(2,3)]

# 중복 조합
from itertools import combinations_with_replacement
list(combinations_with_replacement([1,2,3], 2))

# 데카르트 곱 (중복 순열)
list(product([1,2], repeat=3))     # 2^3 = 8가지
list(product([0,1], [0,1]))        # [(0,0),(0,1),(1,0),(1,1)]
```

---

# 🔥 18. 유용한 내장 함수

```python
abs(-10)                          # 절댓값
round(3.14159, 2)                 # 3.14  (소수점 2자리)
pow(2, 10)                        # 1024  (= 2**10)
pow(2, 10, 1000)                  # (2^10) % 1000  (모듈러 거듭제곱)
divmod(7, 3)                      # (2, 1) → 몫, 나머지
any([False, True, False])         # True  (하나라도 True)
all([True, True, True])           # True  (모두 True)
sum(arr)
max(arr)
min(arr)
max(a, b, c)                      # 여러 인자도 가능
enumerate(arr, start=1)           # 1부터 인덱스 시작
zip(arr1, arr2)                   # 같은 위치 묶기
```

---

# 🔥 19. 난수 (random)

```python
import random

random.random()                # 0.0 이상 1.0 미만 float
random.randint(1, 10)          # 1~10 정수 (양 끝 포함!)
random.randrange(0, 10)        # 0~9 정수 (range처럼)
random.choice([1, 2, 3])       # 리스트에서 1개 선택
random.choices([1,2,3], k=2)   # 중복 허용, k개 선택
random.sample([1,2,3,4], 2)    # 중복 없이 k개 선택
random.shuffle(arr)            # 리스트 섞기 (반환값 없음!)
```

## ❗ 자주 틀리는 것

```python
arr = random.shuffle(arr)    # ❌ None 반환됨!
random.shuffle(arr)          # ✅ 원본을 직접 수정

random.randint(1, 10)        # ✅ 10 포함
random.randrange(1, 10)      # ⚠️ 10 미포함
```

---

# 🔥 20. 날짜와 시간 (datetime)

```python
from datetime import datetime, date, timedelta

now = datetime.now()           # 날짜 + 시간
today = date.today()           # 날짜만

now.year / now.month / now.day
now.hour / now.minute / now.second
now.weekday()                  # 월=0 ~ 일=6
now.isoweekday()               # 월=1 ~ 일=7

d = date(2024, 1, 1)
dt = datetime(2024, 1, 1, 9, 30, 0)

d + timedelta(days=7)          # 7일 후
d - timedelta(weeks=1)         # 1주 전
dt + timedelta(hours=3)        # 3시간 후

diff = d2 - d1
diff.days                      # 일수 차이 (정수)
diff.total_seconds()           # 초 단위 차이

now.strftime("%Y-%m-%d %H:%M:%S")            # datetime → 문자열
datetime.strptime("2024-01-01", "%Y-%m-%d")  # 문자열 → datetime
```

## 🔥 자주 쓰는 포맷 코드

```plaintext
%Y  연도 (2024)    %m  월 (01~12)    %d  일 (01~31)
%H  시 (00~23)     %M  분 (00~59)    %S  초 (00~59)
%A  요일 영문 (Monday...)            %j  연중 몇 번째 날 (001~366)
```

## ❗ 자주 틀리는 것

```python
diff.days          # ✅ 364  ← 숫자로 사용하려면 .days 필요
int(diff)          # ❌ 에러!
now.weekday()      # 월=0, 일=6
now.isoweekday()   # 월=1, 일=7
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
digits = [int(d) for d in str(n)]    # 123 → [1, 2, 3]
```

## 최댓값 인덱스

```python
idx = arr.index(max(arr))
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
a, b = b, a                     # 🔥 스왑 (임시변수 불필요)
a, *rest = [1, 2, 3, 4]         # a=1, rest=[2,3,4]
first, *mid, last = [1,2,3,4]   # first=1, mid=[2,3], last=4
```

## 누적합 패턴

```python
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]
# arr[l:r+1] 합 = prefix[r+1] - prefix[l]
```

---

# 🔥 22. 실수 체크리스트

```plaintext
1.  : 붙였는가? (if, for, def, while 등)
2.  == 썼는가? (= 아님)
3.  True/False 대문자인가?
4.  인덱스 범위 초과 안 했는가?
5.  join 대신 += 안 썼는가? (느림)
6.  IndexError 가능성 체크
7.  문자열 + 숫자 → str() 변환 필수
8.  join 안에 숫자 → str 변환 후
9.  2D 배열 [[0]*m]*n ❌ (같은 행 공유!) → [[0]*m for _ in range(n)]
10. sort()는 원본 변경·반환 None, sorted()는 새 리스트
11. arr.remove(x)는 첫 번째 하나만 제거
12. deque 대신 list.pop(0) 쓰면 O(n)으로 느림
13. 재귀 깊이 기본 1000 → setrecursionlimit 필요 시
14. random.shuffle() 반환값 없음 → 원본 수정됨
15. timedelta 차이 → .days로 꺼내야 숫자 사용 가능
16. sys.stdin.readline 쓸 때 줄 끝 \n → strip() 필수
17. str.find()는 없으면 -1, str.index()는 없으면 ValueError
18. Counter는 없는 키도 0 반환, dict는 KeyError
```

---

# 🚀 핵심 무기 요약

| 상황 | 사용 |
|---|---|
| 문자열 합치기 | `''.join(arr)` |
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
| 메서드 모를 때 | `ord` / `chr` + 조건문으로 직접 |
| 특수문자 출력 | `\\` 탈출 or 삼중따옴표 |
| 숫자+문자 출력 | 콤마(,) or f-string |

---

# 🔥 최종 한 줄

👉 "메서드를 모르면 조건문으로 직접 — 패턴이 보이면 코드가 나온다"