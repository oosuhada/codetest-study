# ☕ Java 코테 치트시트 (Python 비교판)

> Python으로 이미 배운 패턴을 Java로 연결한다.
> 구조는 같고 문법만 다르다.

---

# 🔥 1. 입력 / 출력

## Python
```python
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
print(n)
print(*arr)
```

## Java
```java
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine().trim());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(n);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(arr[i]);
            if (i < n - 1) sb.append(" ");
        }
        System.out.println(sb);
    }
}
```

## 💡 대응표
| Python | Java |
|---|---|
| `int(input())` | `Integer.parseInt(br.readLine().trim())` |
| `input().split()` | `new StringTokenizer(br.readLine())` |
| `print(*arr)` | `StringBuilder`로 모아서 출력 |
| `sys.stdin.readline` | `BufferedReader` (빠른 입력) |

## ❗ 핵심 규칙
- Java는 **무조건 `BufferedReader` + `StringTokenizer`** 쓰기 (`Scanner`는 느려서 시간초과 위험)
- 출력도 `System.out.println` 반복 대신 **`StringBuilder`** 모아서 한 번에

---

# 🔥 2. 반복문

## Python
```python
for i in range(n):
for i in range(1, n+1):
for i in range(n, 0, -1):

for i, v in enumerate(arr):
for a, b in zip(arr1, arr2):
```

## Java
```java
for (int i = 0; i < n; i++) {}
for (int i = 1; i <= n; i++) {}
for (int i = n; i > 0; i--) {}

// 배열 순회 (향상된 for문)
for (int v : arr) {}

// enumerate 대신 → 그냥 인덱스 i 사용
for (int i = 0; i < arr.length; i++) {
    System.out.println(i + " " + arr[i]);
}

// zip 대신 → 인덱스로 접근
for (int i = 0; i < arr1.length; i++) {
    System.out.println(arr1[i] + " " + arr2[i]);
}
```

## 💡 대응표
| Python | Java |
|---|---|
| `range(n)` | `i = 0; i < n; i++` |
| `enumerate(arr)` | 인덱스 `i` 직접 사용 |
| `zip(a, b)` | 인덱스 `i` 직접 사용 |
| `for v in arr` | `for (int v : arr)` |

---

# 🔥 3. 조건문

## Python
```python
if n > 10:
    print("크다")
elif n == 10:
    print("같다")
else:
    print("작다")

if a <= x <= b:   # Python만 가능!
```

## Java
```java
if (n > 10) {
    System.out.println("크다");
} else if (n == 10) {
    System.out.println("같다");
} else {
    System.out.println("작다");
}

if (a <= x && x <= b) {}  // Java는 이렇게

// 삼항연산자
int result = (n > 10) ? 1 : 0;
```

## 💡 대응표
| Python | Java |
|---|---|
| `and` | `&&` |
| `or` | `\|\|` |
| `not` | `!` |
| `elif` | `else if` |
| `a if cond else b` | `cond ? a : b` |
| `a <= x <= b` | `a <= x && x <= b` |

---

# 🔥 4. 배열 / 리스트

## Python
```python
arr = [1, 2, 3]
arr.append(4)
arr.pop()
arr.remove(2)
arr[1:3]
len(arr)
```

## Java — 배열 (크기 고정)
```java
int[] arr = {1, 2, 3};
int[] arr = new int[n];   // 기본값 0으로 초기화

arr.length    // 길이 (len 대신)
```

## Java — ArrayList (크기 가변, Python list와 동일)
```java
import java.util.*;

ArrayList<Integer> list = new ArrayList<>();
list.add(4);           // append
list.remove(list.size()-1);  // pop()
list.remove(Integer.valueOf(2));  // remove(값)
list.get(i);           // arr[i]
list.size();           // len(arr)
list.set(i, 99);       // arr[i] = 99

// 부분 리스트 (슬라이싱)
list.subList(1, 3);    // [1, 3) 인덱스
```

## 💡 대응표
| Python | Java |
|---|---|
| `arr = []` | `ArrayList<Integer> list = new ArrayList<>()` |
| `arr.append(x)` | `list.add(x)` |
| `arr.pop()` | `list.remove(list.size()-1)` |
| `arr[i]` | `list.get(i)` |
| `len(arr)` | `list.size()` 또는 `arr.length` |
| `arr[1:3]` | `list.subList(1, 3)` |

## ❗ int[] vs ArrayList
- **크기 고정** → `int[]` (빠름)
- **크기 변동** → `ArrayList<Integer>` (유연)
- 코테에서는 크기 알면 `int[]`, 모르면 `ArrayList`

---

# 🔥 5. 2차원 배열

## Python
```python
graph = [[0] * m for _ in range(n)]
graph[i][j]
```

## Java
```java
int[][] graph = new int[n][m];   // 기본값 0
graph[i][j] = 1;

// 입력 받기
int[][] graph = new int[n][m];
for (int i = 0; i < n; i++) {
    st = new StringTokenizer(br.readLine());
    for (int j = 0; j < m; j++) {
        graph[i][j] = Integer.parseInt(st.nextToken());
    }
}
```

## 💡 대응표
| Python | Java |
|---|---|
| `[[0]*m for _ in range(n)]` | `new int[n][m]` |
| `graph[i][j]` | `graph[i][j]` (동일) |

---

# 🔥 6. 문자열

## Python
```python
s.upper()   s.lower()   s.strip()
s.split()   s.split(',')
s.replace("l","x")
s.find("e")
s.count("l")
s.isupper() s.islower() s.isalpha() s.isdigit()
"abc" in "abcdef"
''.join(arr)
s[::-1]
```

## Java
```java
s.toUpperCase()   s.toLowerCase()   s.trim()
s.split(" ")      s.split(",")
s.replace("l","x")
s.indexOf("e")      // 없으면 -1 반환
// count 직접 구현 필요

Character.isUpperCase(c)
Character.isLowerCase(c)
Character.isAlphabetic(c)
Character.isDigit(c)
s.contains("abc")

String.join("", arr)           // join
new StringBuilder(s).reverse().toString()  // 뒤집기
```

## 💡 대응표
| Python | Java |
|---|---|
| `s.upper()` | `s.toUpperCase()` |
| `s.split()` | `s.split(" ")` |
| `s.find("e")` | `s.indexOf("e")` |
| `"a" in s` | `s.contains("a")` |
| `''.join(arr)` | `String.join("", arr)` |
| `s[::-1]` | `new StringBuilder(s).reverse().toString()` |
| `s.isdigit()` | `Character.isDigit(c)` — 문자 하나씩 |

## ❗ Java 문자열 핵심 규칙
```java
// 문자열 비교
s1 == s2      // ❌ 주소 비교
s1.equals(s2) // ✅ 내용 비교

// 문자 접근
s.charAt(i)   // s[i] 대신

// 문자열 합치기 (반복 시)
StringBuilder sb = new StringBuilder();
sb.append("hello");
sb.append(123);
String result = sb.toString();   // join 대신
```

---

# 🔥 7. 딕셔너리 → HashMap

## Python
```python
d = {}
d["a"] = 1
d.get("c", 0)
"a" in d
for key, value in d.items():

from collections import defaultdict
d = defaultdict(int)
d["a"] += 1
```

## Java
```java
import java.util.*;

HashMap<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.getOrDefault("c", 0);    // get("c", 0) 대신
map.containsKey("a");        // "a" in d 대신
map.put("a", map.getOrDefault("a", 0) + 1);  // defaultdict 패턴

for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + " " + entry.getValue());
}
```

## 💡 대응표
| Python | Java |
|---|---|
| `d = {}` | `HashMap<String, Integer> map = new HashMap<>()` |
| `d["a"] = 1` | `map.put("a", 1)` |
| `d.get("a", 0)` | `map.getOrDefault("a", 0)` |
| `"a" in d` | `map.containsKey("a")` |
| `d.items()` | `map.entrySet()` |
| `defaultdict(int)` | `map.getOrDefault(key, 0) + 1` 패턴 |

---

# 🔥 8. 집합 → HashSet

## Python
```python
s = set()
s.add(1)
s.remove(1)
1 in s
a & b   a | b   a - b
```

## Java
```java
HashSet<Integer> set = new HashSet<>();
set.add(1);
set.remove(1);
set.contains(1);

// 교집합
set1.retainAll(set2);
// 합집합
set1.addAll(set2);
// 차집합
set1.removeAll(set2);
```

## 💡 대응표
| Python | Java |
|---|---|
| `s.add(x)` | `set.add(x)` |
| `x in s` | `set.contains(x)` |
| `a & b` | `retainAll` |
| `a \| b` | `addAll` |

---

# 🔥 9. 스택 / 큐

## Python
```python
# 스택
stack = []
stack.append(1)
stack.pop()

# 큐
from collections import deque
q = deque()
q.append(1)
q.popleft()
```

## Java
```java
import java.util.*;

// 스택
Stack<Integer> stack = new Stack<>();
stack.push(1);
stack.pop();
stack.peek();    // 맨 위 값 확인 (제거 안 함)
stack.isEmpty();

// 큐 (ArrayDeque 권장)
Queue<Integer> q = new LinkedList<>();
// 또는
ArrayDeque<Integer> q = new ArrayDeque<>();

q.offer(1);     // append
q.poll();       // popleft
q.peek();       // 앞 값 확인
q.isEmpty();
```

## 💡 대응표
| Python | Java |
|---|---|
| `stack.append(x)` | `stack.push(x)` |
| `stack.pop()` | `stack.pop()` |
| `q.append(x)` | `q.offer(x)` |
| `q.popleft()` | `q.poll()` |
| `not stack` | `stack.isEmpty()` |

---

# 🔥 10. 정렬

## Python
```python
arr.sort()
arr.sort(reverse=True)
arr.sort(key=lambda x: x[1])
sorted(arr)
```

## Java — 기본 배열
```java
import java.util.*;

int[] arr = {3, 1, 2};
Arrays.sort(arr);                          // 오름차순

// 내림차순 (기본 배열은 Integer[]로 변환 필요)
Integer[] arr2 = {3, 1, 2};
Arrays.sort(arr2, Collections.reverseOrder());
```

## Java — ArrayList
```java
ArrayList<Integer> list = new ArrayList<>();
Collections.sort(list);                    // 오름차순
Collections.sort(list, Collections.reverseOrder()); // 내림차순

// 람다 정렬 (Python key=lambda와 동일)
list.sort((a, b) -> a - b);               // 오름차순
list.sort((a, b) -> b - a);               // 내림차순

// 2차원 배열 정렬 (두 번째 값 기준)
int[][] arr2d = {{1,3},{2,1},{3,2}};
Arrays.sort(arr2d, (a, b) -> a[1] - b[1]);

// 복합 기준 (두 번째 오름차순, 같으면 첫 번째 내림차순)
Arrays.sort(arr2d, (a, b) -> {
    if (a[1] != b[1]) return a[1] - b[1];
    return b[0] - a[0];
});
```

## 💡 대응표
| Python | Java |
|---|---|
| `arr.sort()` | `Arrays.sort(arr)` |
| `arr.sort(reverse=True)` | `Arrays.sort(arr2, Collections.reverseOrder())` |
| `arr.sort(key=lambda x: x[1])` | `Arrays.sort(arr, (a,b) -> a[1]-b[1])` |
| `sorted(arr)` | `Arrays.stream(arr).sorted().toArray()` |

## ❗ Java 정렬 핵심
- `a - b` → 오름차순 / `b - a` → 내림차순
- 기본 `int[]`는 람다 정렬 불가 → `Integer[]` 또는 `ArrayList<Integer>` 써야 함

---

# 🔥 11. BFS (너비 우선 탐색)

## Python
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

## Java
```java
import java.util.*;

static void bfs(List<List<Integer>> graph, int start, boolean[] visited) {
    Queue<Integer> q = new LinkedList<>();
    q.offer(start);
    visited[start] = true;

    while (!q.isEmpty()) {
        int v = q.poll();
        for (int neighbor : graph.get(v)) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.offer(neighbor);
            }
        }
    }
}
```

## Java — 그리드 BFS
```java
static int[] dx = {0, 0, 1, -1};
static int[] dy = {1, -1, 0, 0};

static int bfs(int[][] graph, int startX, int startY, int endX, int endY) {
    int n = graph.length, m = graph[0].length;
    boolean[][] visited = new boolean[n][m];
    Queue<int[]> q = new LinkedList<>();

    q.offer(new int[]{startX, startY, 1});
    visited[startX][startY] = true;

    while (!q.isEmpty()) {
        int[] cur = q.poll();
        int x = cur[0], y = cur[1], dist = cur[2];

        if (x == endX && y == endY) return dist;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m
                    && !visited[nx][ny] && graph[nx][ny] == 1) {
                visited[nx][ny] = true;
                q.offer(new int[]{nx, ny, dist + 1});
            }
        }
    }
    return -1;
}
```

---

# 🔥 12. DFS (깊이 우선 탐색)

## Python
```python
def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
```

## Java
```java
static void dfs(List<List<Integer>> graph, int v, boolean[] visited) {
    visited[v] = true;
    for (int neighbor : graph.get(v)) {
        if (!visited[neighbor]) {
            dfs(graph, neighbor, visited);
        }
    }
}
```

## ❗ Java DFS 핵심
- Python은 재귀 기본 1000 → Java는 기본 스택 크기 더 큼 (보통 문제없음)
- `visited` 배열은 `static` 또는 파라미터로 넘기기

---

# 🔥 13. 우선순위 큐 (힙)

## Python
```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappop(heap)

# 최대 힙
heapq.heappush(heap, -3)
-heapq.heappop(heap)
```

## Java
```java
import java.util.*;

// 최소 힙 (기본)
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(3);
pq.poll();      // 최솟값 꺼냄
pq.peek();      // 최솟값 확인

// 최대 힙
PriorityQueue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
maxPq.offer(3);
maxPq.poll();   // 최댓값 꺼냄

// 2차원 배열 기준 정렬 (두 번째 값 기준 최소 힙)
PriorityQueue<int[]> pq2 = new PriorityQueue<>((a, b) -> a[1] - b[1]);
pq2.offer(new int[]{1, 3});
```

## 💡 대응표
| Python | Java |
|---|---|
| `heapq.heappush(h, x)` | `pq.offer(x)` |
| `heapq.heappop(h)` | `pq.poll()` |
| 최대 힙: `-x` 트릭 | `new PriorityQueue<>(Collections.reverseOrder())` |

---

# 🔥 14. 순열 / 조합

## Python
```python
from itertools import permutations, combinations
list(permutations([1,2,3], 2))
list(combinations([1,2,3], 2))
```

## Java — 직접 구현 (라이브러리 없음)
```java
// 조합
static void combination(int[] arr, int[] result, int start, int depth, int r) {
    if (depth == r) {
        System.out.println(Arrays.toString(result));
        return;
    }
    for (int i = start; i < arr.length; i++) {
        result[depth] = arr[i];
        combination(arr, result, i + 1, depth + 1, r);
    }
}

// 순열
static void permutation(int[] arr, int depth, boolean[] used, int[] result, int r) {
    if (depth == r) {
        System.out.println(Arrays.toString(result));
        return;
    }
    for (int i = 0; i < arr.length; i++) {
        if (!used[i]) {
            used[i] = true;
            result[depth] = arr[i];
            permutation(arr, depth + 1, used, result, r);
            used[i] = false;
        }
    }
}
```

## ❗ Java 핵심
- Python처럼 `itertools` 없음 → **재귀로 직접 구현**
- 조합: `start` 인덱스로 중복 방지
- 순열: `used[]` 배열로 방문 체크

---

# 🔥 15. 이진 탐색

## Python
```python
from bisect import bisect_left
bisect_left(arr, x)
```

## Java
```java
import java.util.*;

// 라이브러리
int idx = Arrays.binarySearch(arr, x);  // 없으면 음수 반환

// 직접 구현 (lower bound)
static int lowerBound(int[] arr, int x) {
    int left = 0, right = arr.length;
    while (left < right) {
        int mid = (left + right) / 2;
        if (arr[mid] < x) left = mid + 1;
        else right = mid;
    }
    return left;
}
```

## 💡 대응표
| Python | Java |
|---|---|
| `bisect_left(arr, x)` | `lowerBound(arr, x)` 직접 구현 |
| `bisect_right(arr, x)` | `upperBound(arr, x)` 직접 구현 |

---

# 🔥 16. 형변환

## Python
```python
str(a)
int("10")
float("3.14")
list("abc")
```

## Java
```java
String.valueOf(a)          // str(a)
Integer.parseInt("10")     // int("10")  ← 문자열 → int
Double.parseDouble("3.14") // float("3.14") ← 문자열 → double
(int) 3.7                  // int(3.7) → 3 (내림)

// 문자 → 숫자
char c = '5';
int n = c - '0';           // Python: int(c)

// 숫자 → 문자
char ch = (char)(n + '0');

// 문자열 → 문자 배열
char[] chars = s.toCharArray();    // list(s) 대신

// 문자 배열 → 문자열
String result = new String(chars); // ''.join(arr) 대신
```

## 💡 대응표
| Python | Java |
|---|---|
| `str(a)` | `String.valueOf(a)` |
| `int("10")` | `Integer.parseInt("10")` |
| `float("3.14")` | `Double.parseDouble("3.14")` |
| `int(c)` (문자) | `c - '0'` |
| `list(s)` | `s.toCharArray()` |
| `''.join(arr)` | `new String(chars)` |

---

# 🔥 17. 박싱 / 언박싱 (Boxing / Unboxing)

> Java에만 있는 개념 — Python에는 없음

## 핵심 개념

Java는 **기본 타입(primitive)** 과 **참조 타입(wrapper class)** 이 분리되어 있습니다.

| 기본 타입 (primitive) | 래퍼 클래스 (wrapper) |
|---|---|
| `int` | `Integer` |
| `double` | `Double` |
| `long` | `Long` |
| `boolean` | `Boolean` |
| `char` | `Character` |

## 박싱 (Boxing) — 기본 타입 → 래퍼 클래스

```java
int n = 10;
Integer boxed = Integer.valueOf(n);   // 명시적 박싱
Integer boxed2 = n;                   // 자동 박싱 (Auto-boxing) ✅ 자주 씀
```

## 언박싱 (Unboxing) — 래퍼 클래스 → 기본 타입

```java
Integer boxed = 100;
int n = boxed.intValue();  // 명시적 언박싱
int n2 = boxed;            // 자동 언박싱 (Auto-unboxing) ✅ 자주 씀
```

## 🔥 자주 쓰는 parse 메서드 (문자열 → 기본 타입)

```java
// 문자열 → int
int n = Integer.parseInt("100");

// 문자열 → double
double d = Double.parseDouble("3.14");

// 문자열 → long
long l = Long.parseLong("123456789");

// 문자열 → boolean
boolean b = Boolean.parseBoolean("true");

// ⚠️ 주의: 숫자가 아닌 문자 포함 시 NumberFormatException 발생
// Integer.parseInt("100a") → ❌ 에러!
// Integer.parseInt(" 100") → ❌ 에러! (trim() 먼저 해야 함)
int safe = Integer.parseInt("100a".trim()); // 이래도 에러 → 숫자만 있어야 함
```

## 🔥 래퍼 클래스의 유용한 메서드

```java
Integer.MAX_VALUE   // int 최댓값: 2,147,483,647
Integer.MIN_VALUE   // int 최솟값: -2,147,483,648
Integer.toBinaryString(n)  // 2진수 문자열로 변환
Integer.toString(n)        // 숫자 → 문자열 (String.valueOf(n)과 동일)
```

## 언제 래퍼 클래스를 써야 하나?

```java
// ✅ ArrayList, HashMap 등 제네릭에는 래퍼 클래스만 가능
ArrayList<Integer> list = new ArrayList<>();  // int ❌, Integer ✅
HashMap<String, Double> map = new HashMap<>(); // double ❌, Double ✅

// ✅ null 값을 다뤄야 할 때
Integer n = null;  // int는 null 불가

// ✅ 기본 연산에서는 그냥 int, double 써라 (빠름)
int a = 10;
double d = 3.14;
```

## 💡 Python과 비교

Python은 모든 것이 객체라서 박싱/언박싱 개념이 없습니다. Java는 성능을 위해 기본 타입을 따로 두었고, 컬렉션(ArrayList 등)을 쓸 때만 래퍼 클래스로 감싸야 합니다.

```python
# Python: 그냥 다 됨
arr = [1, 2, 3]       # int든 뭐든 그냥 리스트에 넣음
d = {"a": 3.14}       # 타입 구분 없음
```

```java
// Java: 컬렉션엔 래퍼 클래스 필수
ArrayList<Integer> list = new ArrayList<>();  // Integer (래퍼)
int[] arr = {1, 2, 3};                        // int (기본) — 이건 제네릭 아님
```

---

# 🚀 핵심 대응표 최종 요약

| 상황 | Python | Java |
|---|---|---|
| 빠른 입력 | `sys.stdin.readline` | `BufferedReader` |
| 가변 배열 | `list` | `ArrayList<Integer>` |
| 딕셔너리 | `dict` | `HashMap<K,V>` |
| 집합 | `set` | `HashSet<T>` |
| 스택 | `list` + `append/pop` | `Stack<T>` |
| 큐 | `deque` + `popleft` | `ArrayDeque` + `poll` |
| 힙 | `heapq` | `PriorityQueue<T>` |
| 정렬 | `sort(key=lambda)` | `Arrays.sort((a,b)->a-b)` |
| 문자열 합치기 | `''.join(arr)` | `StringBuilder` |
| 순열/조합 | `itertools` | 재귀 직접 구현 |
| 이진탐색 | `bisect` | 직접 구현 |
| 문자열 비교 | `s1 == s2` | `s1.equals(s2)` ← 필수! |
| 문자열 → int | `int("10")` | `Integer.parseInt("10")` |
| 문자열 → double | `float("3.14")` | `Double.parseDouble("3.14")` |
| 컬렉션 타입 | `list`, `dict` | `ArrayList<Integer>`, `HashMap<K,V>` (래퍼 클래스) |

---

# ❗ Python → Java 전환 시 절대 실수하면 안 되는 것

```plaintext
1. 문자열 비교는 반드시 .equals()       (== 쓰면 항상 false 가능)
2. int[] 는 람다 정렬 불가              (Integer[] 또는 ArrayList 써야 함)
3. Scanner 쓰면 시간초과                (BufferedReader 써라)
4. System.out.println 반복은 느림      (StringBuilder 모아서 한 번에)
5. 제네릭에 int 못 씀                   (Integer, Long, Double 래퍼 클래스 써야 함)
6. char - '0' 으로 숫자 변환            (int(c) 같은 거 없음)
7. 배열 길이는 .length                  (ArrayList는 .size())
8. parseInt / parseDouble 에 숫자 외 문자 넣으면 NumberFormatException
9. trim() 안 하면 공백 포함돼서 parseInt 에러 날 수 있음
```

---

# 🔥 최종 한 줄

👉 "구조는 Python과 같다 — 자료구조 클래스 이름과 메서드명만 다르게 바꿔라"