# 🚀 Python 코테 패턴 치트시트 (문제 → 풀이 연결 완전판)

---

# 📌 패턴 분류

| 분류 | 패턴 번호 |
|---|---|
| 입출력 기본 | 0-1 ~ 0-5 |
| 문자열 처리 | 1 ~ 6 |
| 수학 / 조건 | 7 ~ 10 |
| 리스트 / 정렬 | 11 ~ 15 |
| 딕셔너리 / 집합 | 16 ~ 18 |
| 스택 / 큐 | 19 ~ 21 |
| 완전탐색 (DFS/BFS) | 22 ~ 25 |
| 이진탐색 | 26 ~ 27 |
| 순열 / 조합 | 28 ~ 29 |
| 재귀 | 30 |
| 날짜와 시간 | 31 ~ 35 |

---

# 🔥 입출력 기본

---

## 🔥 0-1. 따옴표 충돌 — 이스케이프 출력

### 🧩 문제 유형
문자열 안에 따옴표나 특수문자를 그대로 출력해야 할 때

### ✅ 패턴

```python
# ── 방법 A: 바깥/안쪽 따옴표 종류를 다르게 ──────────────
# 큰따옴표로 감싸면 → 안에 작은따옴표 자유롭게 사용
print("I'm fine")          # 출력: I'm fine
print("It's a nice day")   # 출력: It's a nice day

# 작은따옴표로 감싸면 → 안에 큰따옴표 자유롭게 사용
print('He said "hi"')      # 출력: He said "hi"

# ── 방법 B: 같은 종류 충돌 → 백슬래시(\)로 탈출 ─────────
# \' 는 "문자열 끝"이 아니라 "작은따옴표 글자"로 인식
print('I\'m fine')         # 출력: I'm fine
print("He said \"hi\"")    # 출력: He said "hi"

# 백슬래시 자체 출력 → \\ (두 번 써야 \ 하나 출력)
print("C:\\Users\\kim")    # 출력: C:\Users\kim

# ── 방법 C: 삼중따옴표(""") ───────────────────────────
# 언제 쓰나?
#   1. 작은따옴표 + 큰따옴표가 동시에 들어갈 때 → 탈출 불필요
#   2. 여러 줄 문자열을 코드에 그대로 쓰고 싶을 때
print("""It's a "test".""")  # 출력: It's a "test".

# 여러 줄 출력 — \n 없이 Enter로 줄바꿈 가능
print("""1번 줄
2번 줄
3번 줄""")
# 출력:
# 1번 줄
# 2번 줄
# 3번 줄
```

### 💡 핵심
| 상황 | 해결책 |
|---|---|
| 문자열에 `'` 포함 | 바깥을 `"..."` 로 감싸기 |
| 문자열에 `"` 포함 | 바깥을 `'...'` 로 감싸기 |
| `'` 와 `"` 동시에 포함 | `"""..."""` 삼중따옴표 |
| 같은 따옴표가 충돌 | `\'` 또는 `\"` 로 탈출 |
| `\` 자체 출력 | `\\` 두 번 |

---

## 🔥 0-2. 특수문자 / 공백 제어 출력

### 🧩 문제 유형
줄바꿈, 탭, 빈 줄 등을 특정 위치에 출력해야 할 때

### ✅ 패턴

```python
# ── \n : 줄바꿈 ────────────────────────────────────────
# print()는 기본적으로 마지막에 \n을 자동 삽입함
# 문자열 중간에 \n을 넣으면 그 위치에서 줄이 바뀜
print("줄1\n줄2\n줄3")
# 출력:
# 줄1
# 줄2
# 줄3

# ── \t : 탭 간격 ────────────────────────────────────────
# 탭 위치까지 공백을 채워줌 (보통 4~8칸)
print("이름\t나이")
print("홍길동\t25")
# 출력:
# 이름    나이
# 홍길동  25

# ── end 옵션 : print 마지막 문자 변경 ──────────────────
# 기본값: end="\n" (줄바꿈)
# end="" 로 바꾸면 → 줄바꿈 없이 이어서 출력

for i in range(1, 4):
    print(i, end=" ")   # 줄바꿈 대신 공백으로 끝냄
# 출력: 1 2 3           ← 한 줄에 이어짐

print()   # ← 루프 뒤에 빈 print()로 줄바꿈 마무리 (코테 습관!)

# ── 빈 줄 출력 ──────────────────────────────────────────
print("위")
print()            # 인자 없이 → 빈 줄 1개
print("아래")
# 출력:
# 위
#
# 아래
```

### 💡 핵심
- `\n` 줄바꿈, `\t` 탭, `\\` 백슬래시
- `end=""` → 줄바꿈 없이 같은 줄에 이어붙임
- `end=" "` → 공백으로 구분하며 이어붙임
- 반복문에서 `end=""` 쓴 뒤 → 마지막에 `print()` 로 줄바꿈 마무리

---

## 🔥 0-3. 숫자 + 문자열 혼합 출력

### 🧩 문제 유형
숫자와 문자열을 조합해서 특정 형식으로 출력해야 할 때

### ✅ 패턴

```python
a, b = 4, 5

# ── 방법1: 콤마(,) — 코테 추천 ──────────────────────────
# 각 항목 자동으로 str 변환 + 사이에 공백 1칸 자동 삽입
print(a, "+", b, "=", a + b)    # 출력: 4 + 5 = 9
print(a, b, sep=",")            # 출력: 4,5    ← 구분자 변경
print(a, b, sep="")             # 출력: 45     ← 구분자 없이 붙이기

# ── 방법2: f-string — 가독성 최고 ────────────────────────
# {} 안에 변수나 식을 넣으면 값으로 자동 치환
print(f"{a} + {b} = {a + b}")  # 출력: 4 + 5 = 9
print(f"결과: {a * b}")         # 출력: 결과: 20

# ── 방법3: + 연산 — 주의 필요 ────────────────────────────
# + 는 같은 타입끼리만 연결됨 (문자열 + 문자열)
# 숫자를 넣으면 TypeError 발생 → str()로 변환 필수
print("a = " + str(a))         # 출력: a = 4  ✅
# print("a = " + a)            # ❌ TypeError: can only concatenate str (not "int") to str
```

### 💡 핵심
- 콤마(,) → 자동 공백, 타입 변환 불필요 → 코테 최속
- f-string → 가장 읽기 쉬움, 포맷 지정도 가능
- `+` 연산 → 숫자면 반드시 `str()` 감쌀 것 (빼먹으면 런타임 에러)

---

## 🔥 0-4. 숫자 포맷 출력

### 🧩 문제 유형
소수점 자릿수 고정, 앞에 0 패딩, 천 단위 쉼표 등 특정 형식으로 출력

### ✅ 패턴

```python
# ── 소수점 자릿수 고정 ────────────────────────────────────
# f"{값:.Nf}" → N자리까지 표시, 나머지는 반올림
print(f"{3.14159:.2f}")     # 출력: 3.14    ← 소수점 2자리
print(f"{3.14159:.4f}")     # 출력: 3.1416  ← 소수점 4자리 (반올림!)
print(f"{3:.2f}")           # 출력: 3.00    ← 정수도 소수점 붙여 출력

# ── 0 패딩 ────────────────────────────────────────────────
# f"{값:0Nd}" → 총 N자리, 빈 자리를 0으로 채움
# 예: 시간/날짜 표현에 자주 등장 (09:05:07)
print(f"{7:05d}")           # 출력: 00007   ← 총 5자리
print(f"{42:05d}")          # 출력: 00042
print(f"{12345:05d}")       # 출력: 12345   ← 이미 5자리면 그대로

# ── 천 단위 쉼표 ──────────────────────────────────────────
print(f"{1000000:,}")       # 출력: 1,000,000
print(f"{9876543:,}")       # 출력: 9,876,543

# ── 문자열 정렬 ───────────────────────────────────────────
# f"{값:>N}" 오른쪽, f"{값:<N}" 왼쪽, f"{값:^N}" 가운데
print(f"{'hi':>10}")        # 출력:         hi  (오른쪽 정렬)
print(f"{'hi':<10}")        # 출력: hi          (왼쪽 정렬)
print(f"{'hi':^10}")        # 출력:     hi      (가운데 정렬)
```

### 💡 핵심
| 포맷 | 의미 | 예시 |
|---|---|---|
| `:.2f` | 소수점 2자리 (반올림) | `3.14159` → `3.14` |
| `:05d` | 총 5자리, 빈 자리 0으로 | `42` → `00042` |
| `:,` | 천 단위 쉼표 | `1000000` → `1,000,000` |
| `:>10` | 오른쪽 정렬 (총 10칸) | `hi` → `        hi` |

---

## 🔥 0-5. 리스트 출력 패턴

### 🧩 문제 유형
리스트를 공백/줄바꿈/특정 구분자로 출력해야 할 때

### ✅ 패턴

```python
arr = [1, 2, 3, 4, 5]

# ── print(arr) vs print(*arr) ─────────────────────────────
print(arr)                     # 출력: [1, 2, 3, 4, 5]  ← 대괄호 포함 → 코테 오답!
print(*arr)                    # 출력: 1 2 3 4 5         ← 대괄호 없이 공백 구분 → 정답 형식

# *arr 의 원리: 리스트를 풀어서 개별 인자로 전달
# print(*[1,2,3]) == print(1, 2, 3)

# ── 구분자 변경 ──────────────────────────────────────────
print(*arr, sep=",")           # 출력: 1,2,3,4,5
print(*arr, sep=" | ")         # 출력: 1 | 2 | 3 | 4 | 5

# ── join 으로 이어붙이기 ──────────────────────────────────
# join은 문자열 리스트만 가능 → 숫자는 map(str, arr) 필수
print(' '.join(map(str, arr))) # 출력: 1 2 3 4 5
print(','.join(map(str, arr))) # 출력: 1,2,3,4,5

# ── 한 원소씩 세로 출력 ──────────────────────────────────
for x in arr:
    print(x)
# 출력:
# 1
# 2
# 3
# 4
# 5

# ── 2D 리스트 출력 ────────────────────────────────────────
matrix = [[1, 2, 3], [4, 5, 6]]
for row in matrix:
    print(*row)
# 출력:
# 1 2 3
# 4 5 6
```

### 💡 핵심
- `print(arr)` → `[1, 2, 3]` 대괄호 포함 → **코테에서 거의 오답**
- `print(*arr)` → `1 2 3` 대괄호 없음 → **코테 정답 형식**
- 숫자 리스트 `join` → `map(str, arr)` 변환 먼저

---

# 🔥 문자열 처리

---

## 🔥 1. 두 문자열 번갈아 합치기

### 🧩 문제 유형
두 문자열 str1, str2를 번갈아 합쳐라. str1이 더 길면 나머지를 뒤에 붙여라.

### ✅ 패턴

```python
def solution(str1, str2):
    result = []
    for a, b in zip(str1, str2):
        result.append(a)
        result.append(b)
    # zip은 짧은 쪽 기준이라 남은 부분 처리 필요
    if len(str1) > len(str2):
        result.append(str1[len(str2):])
    else:
        result.append(str2[len(str1):])
    return ''.join(result)
```

### 💡 핵심
- `zip` → 두 문자열 동시 순회
- `join` → 리스트를 문자열로 합치기
- 길이 차이 처리 주의

---

## 🔥 2. 문자열 뒤집기

### 🧩 문제 유형
문자열을 뒤집어라

### ✅ 패턴

```python
def solution(s):
    return s[::-1]
```

### 다른 방법

```python
def solution(s):
    return ''.join(reversed(s))
```

---

## 🔥 3. 문자열 대소문자 변환

### 🧩 문제 유형
대문자 → 소문자, 소문자 → 대문자로 바꿔라 (각 문자 반전)

### ✅ 패턴

```python
def solution(s):
    result = []
    for c in s:
        if c.isupper():
            result.append(c.lower())
        else:
            result.append(c.upper())
    return ''.join(result)
```

### 더 짧은 방법

```python
def solution(s):
    return s.swapcase()
```

---

## 🔥 4. 문자열 압축 (런렝스 인코딩)

### 🧩 문제 유형
"aaabbc" → "a3b2c1" 같이 연속된 문자를 개수와 함께 표현

### ✅ 패턴

```python
def solution(s):
    result = []
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            result.append(s[i-1] + str(cnt))
            cnt = 1
    result.append(s[-1] + str(cnt))
    return ''.join(result)
```

### 💡 핵심
- 이전 문자와 현재 문자 비교
- 마지막 문자 처리 잊지 말기

---

## 🔥 5. 팰린드롬 (회문) 판별

### 🧩 문제 유형
앞에서 읽어도 뒤에서 읽어도 같은 문자열인지 판별

### ✅ 패턴

```python
def solution(s):
    return s == s[::-1]
```

### 숫자로 판별

```python
def solution(n):
    s = str(n)
    return s == s[::-1]
```

---

## 🔥 6. 숫자 이어붙이기 비교 (최대 수 만들기)

### 🧩 문제 유형
[3, 30, 34, 5, 9] → 배열을 이어 붙여 가장 큰 수 만들기

### ✅ 패턴

```python
from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))

    def compare(a, b):
        if a + b > b + a:
            return -1   # a를 앞에
        elif a + b < b + a:
            return 1    # b를 앞에
        else:
            return 0

    numbers.sort(key=cmp_to_key(compare))
    answer = ''.join(numbers)

    # 전부 0이면 "0" 반환
    return '0' if answer[0] == '0' else answer
```

### 💡 핵심
- 두 숫자를 이어붙여 크기 비교
- `cmp_to_key` 로 사용자 정의 정렬

---

# 🔥 수학 / 조건

---

## 🔥 7. 나눠떨어지는지 체크

### 🧩 문제 유형
num이 n으로 나눠떨어지면 1, 아니면 0

### ✅ 패턴

```python
def solution(num, n):
    return 1 if num % n == 0 else 0
```

---

## 🔥 8. 여러 조건 동시 체크

### 🧩 문제 유형
number가 n과 m 둘 다 나눠떨어지면 1, 아니면 0

### ✅ 패턴

```python
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0
```

---

## 🔥 9. 소수 판별

### 🧩 문제 유형
n이 소수인지 판별하라

### ✅ 패턴

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### 여러 수 소수 판별 (에라토스테네스의 체)

```python
def solution(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sum(sieve)   # 소수 개수
```

### 💡 핵심
- √n까지만 확인
- 에라토스테네스의 체: 범위 내 모든 소수

---

## 🔥 10. GCD / LCM (최대공약수 / 최소공배수)

### 🧩 문제 유형
두 수의 최대공약수, 최소공배수 구하기

### ✅ 패턴

```python
import math
math.gcd(a, b)           # 최대공약수
a * b // math.gcd(a, b)  # 최소공배수
```

### 직접 구현 (유클리드 호제법)

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
```

---

# 🔥 리스트 / 정렬

---

## 🔥 11. 리스트 합 / 최대 / 최소

### ✅ 패턴

```python
sum(arr)
max(arr)
min(arr)
max(arr, key=lambda x: x[1])   # 특정 기준 최대
```

---

## 🔥 12. K번째 최솟값 / 최댓값

### 🧩 문제 유형
배열에서 k번째로 작은 값 반환

### ✅ 패턴

```python
def solution(arr, k):
    arr.sort()
    return arr[k - 1]
```

---

## 🔥 13. 특정 기준 정렬

### 🧩 문제 유형
단어를 길이 기준, 같으면 사전순 정렬

### ✅ 패턴

```python
def solution(arr):
    arr.sort(key=lambda x: (len(x), x))
    return arr
```

### 이중 기준 정렬

```python
# 두 번째 값 오름차순, 같으면 첫 번째 값 내림차순
arr.sort(key=lambda x: (x[1], -x[0]))
```

---

## 🔥 14. 2차원 배열 정렬

### 🧩 문제 유형
[이름, 점수] 형태 리스트를 점수 내림차순, 같으면 이름 오름차순

### ✅ 패턴

```python
def solution(arr):
    arr.sort(key=lambda x: (-x[1], x[0]))
    return arr
```

---

## 🔥 15. 연속 부분 배열의 합

### 🧩 문제 유형
합이 k인 연속 부분 배열의 개수 구하기

### ✅ 패턴 (투포인터)

```python
def solution(arr, k):
    count = 0
    left = 0
    total = 0
    for right in range(len(arr)):
        total += arr[right]
        while total > k and left <= right:
            total -= arr[left]
            left += 1
        if total == k:
            count += 1
    return count
```

### 💡 핵심
- 투포인터: left, right 두 포인터로 범위 조절
- 양수 배열일 때만 사용 가능

---

# 🔥 딕셔너리 / 집합

---

## 🔥 16. 카운트 / 빈도수

### 🧩 문제 유형
각 원소의 개수를 세라

### ✅ 패턴

```python
from collections import Counter

def solution(arr):
    cnt = Counter(arr)
    return cnt.most_common(1)[0][0]   # 가장 많은 원소
```

### 직접 구현

```python
def solution(arr):
    d = {}
    for x in arr:
        d[x] = d.get(x, 0) + 1
    return d
```

---

## 🔥 17. 두 배열 비교 (아나그램)

### 🧩 문제 유형
두 문자열이 서로 애너그램인지 판별 (같은 문자로 구성)

### ✅ 패턴

```python
from collections import Counter

def solution(s1, s2):
    return Counter(s1) == Counter(s2)
```

---

## 🔥 18. 중복 제거 후 개수

### 🧩 문제 유형
배열에서 서로 다른 원소 개수

### ✅ 패턴

```python
def solution(arr):
    return len(set(arr))
```

---

# 🔥 스택 / 큐

---

## 🔥 19. 괄호 짝 맞추기

### 🧩 문제 유형
괄호 문자열이 올바른지 판별

### ✅ 패턴

```python
def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
```

### 💡 핵심
- 여는 괄호 → push
- 닫는 괄호 → pop (비어있으면 False)
- 마지막에 stack이 비어있어야 True

---

## 🔥 20. 기능 개발 (큐 시뮬레이션)

### 🧩 문제 유형
각 작업의 진도와 속도가 주어졌을 때, 배포 횟수와 배포별 기능 수

### ✅ 패턴

```python
import math
from collections import deque

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    q = deque(days)
    answer = []

    while q:
        max_day = q.popleft()
        count = 1
        while q and q[0] <= max_day:
            q.popleft()
            count += 1
        answer.append(count)

    return answer
```

---

## 🔥 21. 다리를 지나는 트럭 (큐 시뮬레이션)

### 🧩 문제 유형
다리 길이, 최대 하중, 트럭 무게 배열 → 모든 트럭이 건너는 시간

### ✅ 패턴

```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    current_weight = 0
    time = 0

    for truck in truck_weights:
        while True:
            if current_weight + truck <= weight:
                removed = bridge.popleft()
                current_weight -= removed
                bridge.append(truck)
                current_weight += truck
                time += 1
                break
            else:
                removed = bridge.popleft()
                current_weight -= removed
                bridge.append(0)
                time += 1

    time += bridge_length   # 마지막 트럭이 다 건너는 시간
    return time
```

---

# 🔥 완전탐색 (DFS/BFS)

---

## 🔥 22. 미로 탈출 (BFS 최단 거리)

### 🧩 문제 유형
N×M 미로에서 시작→도착 최단 거리

### ✅ 패턴

```python
from collections import deque

def solution(graph, start_x, start_y, end_x, end_y):
    n = len(graph)
    m = len(graph[0])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False] * m for _ in range(n)]

    q = deque([(start_x, start_y, 1)])
    visited[start_x][start_y] = True

    while q:
        x, y, dist = q.popleft()
        if x == end_x and y == end_y:
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
    return -1
```

### 💡 핵심
- BFS = 최단 거리 보장
- 상하좌우 4방향 이동
- 범위 체크 + 방문 체크

---

## 🔥 23. 섬 개수 세기 (DFS 연결 요소)

### 🧩 문제 유형
1은 육지, 0은 바다 → 섬의 개수

### ✅ 패턴

```python
def solution(graph):
    n = len(graph)
    m = len(graph[0])
    visited = [[False] * m for _ in range(n)]
    count = 0

    def dfs(x, y):
        visited[x][y] = True
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count
```

---

## 🔥 24. 타겟 넘버 (DFS 완전탐색)

### 🧩 문제 유형
숫자에 + 또는 - 붙여서 타겟 숫자 만드는 경우의 수

### ✅ 패턴

```python
def solution(numbers, target):
    answer = 0

    def dfs(idx, total):
        nonlocal answer
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])

    dfs(0, 0)
    return answer
```

### 💡 핵심
- `nonlocal` → 외부 변수 수정
- 재귀 종료 조건 (idx == len)
- 두 갈래로 분기 (+, -)

---

## 🔥 25. 단어 변환 (BFS 최단 경로)

### 🧩 문제 유형
한 번에 한 글자씩 바꿔 begin → target 최소 변환 횟수

### ✅ 패턴

```python
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    def diff_count(a, b):
        return sum(1 for x, y in zip(a, b) if x != y)

    q = deque([(begin, 0)])
    visited = set()

    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for w in words:
            if w not in visited and diff_count(word, w) == 1:
                visited.add(w)
                q.append((w, cnt + 1))

    return 0
```

---

# 🔥 이진탐색

---

## 🔥 26. 특정 값 이상인 첫 위치

### 🧩 문제 유형
정렬된 배열에서 x 이상인 첫 번째 인덱스

### ✅ 패턴

```python
from bisect import bisect_left

def solution(arr, x):
    arr.sort()
    return bisect_left(arr, x)
```

### 직접 구현

```python
def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left
```

---

## 🔥 27. 범위 내 원소 개수

### 🧩 문제 유형
정렬된 배열에서 left ≤ x ≤ right 인 원소 개수

### ✅ 패턴

```python
from bisect import bisect_left, bisect_right

def solution(arr, left, right):
    arr.sort()
    return bisect_right(arr, right) - bisect_left(arr, left)
```

---

# 🔥 순열 / 조합

---

## 🔥 28. 조합으로 합 만들기

### 🧩 문제 유형
주어진 숫자들로 만들 수 있는 합의 종류

### ✅ 패턴

```python
from itertools import combinations

def solution(numbers):
    result = set()
    for r in range(1, len(numbers) + 1):
        for combo in combinations(numbers, r):
            result.add(sum(combo))
    return len(result)
```

---

## 🔥 29. 순열로 만들 수 있는 최댓값

### 🧩 문제 유형
주어진 숫자로 만들 수 있는 모든 순열 중 특정 조건 만족하는 것 찾기

### ✅ 패턴

```python
from itertools import permutations

def solution(numbers):
    result = set()
    for r in range(1, len(numbers) + 1):
        for perm in permutations(numbers, r):
            result.add(int(''.join(map(str, perm))))
    return len(result)
```

---

# 🔥 재귀

---

## 🔥 30. 피보나치 (메모이제이션)

### 🧩 문제 유형
피보나치 수열 n번째 값

### ✅ 패턴

```python
# 재귀 + 메모이제이션
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### 반복문 (더 빠름)

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

---

# 🔥 날짜와 시간

---

## 🔥 31. 두 날짜 사이 일수 계산 (D-day)

### 🧩 문제 유형
두 날짜가 주어졌을 때 며칠 차이인지 구하라

### ✅ 패턴 — datetime 라이브러리

```python
from datetime import date

def solution(year1, month1, day1, year2, month2, day2):
    d1 = date(year1, month1, day1)
    d2 = date(year2, month2, day2)
    return (d2 - d1).days    # timedelta.days로 정수 추출
```

### ✅ 패턴 — 기본 구현 (라이브러리 없이)

```python
def solution(year1, month1, day1, year2, month2, day2):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def to_days(y, m, d):
        total = 0
        for year in range(1, y):
            total += 366 if is_leap(year) else 365
        for month in range(1, m):
            total += days_in_month[month]
            if month == 2 and is_leap(y):
                total += 1
        total += d
        return total

    return to_days(year2, month2, day2) - to_days(year1, month1, day1)
```

### 💡 핵심
- `(d2 - d1).days` → 반드시 `.days`로 정수 추출 (그냥 `d2 - d1`은 timedelta 객체)
- 기본 구현 시 윤년 처리 필수

---

## 🔥 32. 요일 구하기

### 🧩 문제 유형
특정 날짜가 무슨 요일인지 구하라

### ✅ 패턴 — datetime 라이브러리

```python
from datetime import date

def solution(year, month, day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    d = date(year, month, day)
    return days[d.weekday()]   # weekday(): 월=0 ~ 일=6
```

### ✅ 패턴 — 기본 구현 (젤러의 공식)

```python
def solution(year, month, day):
    # 젤러의 공식: 1월, 2월은 전년도 13, 14월로 처리
    if month <= 2:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    # h: 0=토, 1=일, 2=월, 3=화, 4=수, 5=목, 6=금
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]
```

### 💡 핵심
- `weekday()` → 월=0, 일=6
- `isoweekday()` → 월=1, 일=7 (헷갈리면 이쪽이 더 직관적)
- 기본 구현은 젤러의 공식 — 외우기 어려우면 datetime 써라

---

## 🔥 33. 윤년 판별

### 🧩 문제 유형
주어진 연도가 윤년인지 판별하라

### ✅ 패턴 — 직접 구현 (조건 정확히 외우기)

```python
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```

### ✅ 패턴 — datetime 라이브러리

```python
import calendar

def is_leap(year):
    return calendar.isleap(year)
```

### 💡 핵심 — 윤년 조건 (순서대로 체크)
```plaintext
1. 4로 나눠지면 → 윤년 후보
2. 근데 100으로도 나눠지면 → 윤년 아님
3. 근데 400으로도 나눠지면 → 다시 윤년
예) 2000 → 윤년 / 1900 → 윤년 아님 / 2024 → 윤년
```

---

## 🔥 34. 날짜 유효성 검사

### 🧩 문제 유형
입력된 날짜가 실제로 존재하는 날짜인지 판별하라

### ✅ 패턴 — datetime 라이브러리 (try-except 활용)

```python
from datetime import date

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False
```

### ✅ 패턴 — 기본 구현

```python
def is_valid_date(year, month, day):
    if month < 1 or month > 12:
        return False
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    return 1 <= day <= days_in_month[month]
```

### 💡 핵심
- `try-except ValueError` 패턴 → 가장 간결하고 실수 없음
- 기본 구현 시 윤년 → 2월 29일 처리 잊지 말기

---

## 🔥 35. n일 후 날짜 계산

### 🧩 문제 유형
특정 날짜에서 n일 후(또는 전)의 날짜를 구하라

### ✅ 패턴 — datetime 라이브러리

```python
from datetime import date, timedelta

def solution(year, month, day, n):
    d = date(year, month, day)
    result = d + timedelta(days=n)    # n일 후
    return result.year, result.month, result.day
```

### ✅ 패턴 — 기본 구현

```python
def solution(year, month, day, n):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    for _ in range(n):
        days_in_month[2] = 29 if is_leap(year) else 28
        day += 1
        if day > days_in_month[month]:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1

    return year, month, day
```

### 💡 핵심
- `timedelta(days=n)` → 음수면 n일 전
- 기본 구현 시 월 넘김 → 연도 넘김 순서로 처리
- n이 크면 기본 구현은 느림 → datetime 써라

---

# 🚀 최종 핵심 — 문제 보면 바로 떠올려라

```plaintext
따옴표 충돌 출력       → \' \" 탈출 or 삼중따옴표
줄바꿈 / 탭 출력      → \n \t
같은 줄 이어쓰기      → print(..., end="")
숫자 + 문자 혼합      → f-string or 콤마(,)
소수점 자릿수         → f"{x:.2f}"
0 패딩               → f"{x:05d}"
천 단위 쉼표          → f"{x:,}"
리스트 한 줄 출력      → print(*arr) or ' '.join(map(str, arr))
문자열 합치기        → join
두 개 동시 반복      → zip
인덱스 필요          → enumerate
정렬                → sort / sorted + key
카운트              → Counter
중복 제거            → set
괄호 / 뒤로가기      → 스택 (list)
BFS 최단거리        → deque
DFS 완전탐색        → 재귀
그리드 탐색          → dx/dy + visited
최솟값 우선          → heapq
조합/순열            → itertools
이진탐색             → bisect / 직접 구현
소수 판별            → 에라토스테네스의 체
재귀 최적화          → lru_cache
날짜 차이            → (d2 - d1).days
요일 구하기          → date.weekday()
n일 후 날짜          → date + timedelta(days=n)
윤년 판별            → (y%4==0 and y%100!=0) or y%400==0
날짜 유효성          → try: date(y,m,d) except ValueError
```

---

# 🔥 최종 한 줄

👉 "문제 유형을 보면 코드가 자동으로 떠오르는 상태가 목표다 — 패턴은 외우는 게 아니라 반복해서 손에 익히는 것이다"