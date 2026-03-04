# 🚀 Python 코테 패턴 치트시트 (문제 → 풀이 연결 완전판)

---

# 📌 패턴 분류

| 분류 | 패턴 번호 |
|---|---|
| 문자열 처리 | 1 ~ 6 |
| 수학 / 조건 | 7 ~ 10 |
| 리스트 / 정렬 | 11 ~ 15 |
| 딕셔너리 / 집합 | 16 ~ 18 |
| 스택 / 큐 | 19 ~ 21 |
| 완전탐색 (DFS/BFS) | 22 ~ 25 |
| 이진탐색 | 26 ~ 27 |
| 순열 / 조합 | 28 ~ 29 |
| 재귀 | 30 |

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

# 🚀 최종 핵심 — 문제 보면 바로 떠올려라

```plaintext
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
```

---

# 🔥 최종 한 줄

👉 "문제 유형을 보면 코드가 자동으로 떠오르는 상태가 목표다 — 패턴은 외우는 게 아니라 반복해서 손에 익히는 것이다"