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

# 🔥 4. 배열 / List 컬렉션

> Java List 컬렉션 3종: `ArrayList` (일반), `Vector` (동기화), `LinkedList` (앞뒤 삽입/삭제)

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
arr.length                // 길이
```

## Java — ArrayList (가장 많이 씀 ✅)
```java
import java.util.*;

ArrayList<Integer> list = new ArrayList<>();
```

## Java — Vector (ArrayList와 거의 동일, 멀티스레드 환경에서 안전)
```java
Vector<Integer> vector = new Vector<>();
// 메소드는 ArrayList와 동일 — 코테에서는 거의 안 씀
```

## Java — LinkedList (앞/뒤 삽입·삭제가 빠름, 큐/덱으로도 사용)
```java
LinkedList<Integer> linked = new LinkedList<>();
linked.addFirst(1);   // 맨 앞에 추가
linked.addLast(2);    // 맨 뒤에 추가
linked.removeFirst(); // 맨 앞 제거
linked.removeLast();  // 맨 뒤 제거
```

## 🔥 List 공통 메소드 (추가 / 검색 / 삭제)

```java
// ✅ 객체 추가
list.add(값);            // 끝에 추가      ← arr.append(x)
list.add(인덱스, 값);    // 특정 위치 삽입 ← arr.insert(i, x)
list.set(인덱스, 값);    // 특정 위치 교체 ← arr[i] = x

// ✅ 객체 검색
list.get(인덱스);        // 값 가져오기    ← arr[i]
list.size();             // 원소 수        ← len(arr)
list.isEmpty();          // 비었는지       ← not arr
list.contains(값);       // 포함 여부      ← x in arr
list.indexOf(값);        // 첫 번째 인덱스 ← arr.index(x)

// ✅ 객체 삭제
list.remove(인덱스);            // 인덱스로 삭제  ← arr.pop(i)
list.remove(Integer.valueOf(값)); // 값으로 삭제   ← arr.remove(x)
list.clear();                    // 전체 삭제      ← arr.clear()
```

## 💡 대응표
| Python | Java |
|---|---|
| `arr = []` | `ArrayList<Integer> list = new ArrayList<>()` |
| `arr.append(x)` | `list.add(x)` |
| `arr.insert(i, x)` | `list.add(i, x)` |
| `arr[i]` | `list.get(i)` |
| `arr[i] = x` | `list.set(i, x)` |
| `len(arr)` | `list.size()` 또는 `arr.length` |
| `x in arr` | `list.contains(x)` |
| `arr.index(x)` | `list.indexOf(x)` |
| `arr.pop(i)` | `list.remove(i)` |
| `arr.remove(x)` | `list.remove(Integer.valueOf(x))` |
| `arr.clear()` | `list.clear()` |
| `arr[1:3]` | `list.subList(1, 3)` |

## ❗ int[] vs ArrayList vs LinkedList
- **크기 고정, 빠른 접근** → `int[]`
- **크기 변동, 일반적** → `ArrayList<Integer>` ← 코테에서 주로 이것
- **앞뒤 삽입/삭제 빈번** → `LinkedList<Integer>`
- **큐/덱** → `LinkedList` 또는 `ArrayDeque`

## ❗ remove() 실수 주의
```java
list.remove(1);                  // ⚠️ 인덱스 1 제거 (두 번째 원소)
list.remove(Integer.valueOf(1)); // ✅ 값 1 제거
// 정수 리스트에서 값으로 지울 땐 반드시 Integer.valueOf() 감싸기!
```

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

# 🔥 7. Map 컬렉션 → HashMap / Hashtable / TreeMap / Properties

> Java Map 컬렉션 4종: `HashMap` (일반), `Hashtable` (동기화), `TreeMap` (정렬), `Properties` (문자열 전용)

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

## Java — HashMap (순서 없음 ✅ 가장 많이 씀)
```java
import java.util.*;

HashMap<String, Integer> map = new HashMap<>();
```

## Java — Hashtable (HashMap과 동일하지만 멀티스레드 안전, 구버전)
```java
Hashtable<String, Integer> table = new Hashtable<>();
// null 키/값 불가 (HashMap은 가능) — 코테에서는 거의 안 씀
```

## Java — TreeMap (키 기준 자동 오름차순 정렬)
```java
TreeMap<String, Integer> treeMap = new TreeMap<>();
treeMap.firstKey();          // 가장 작은 키
treeMap.lastKey();           // 가장 큰 키
treeMap.lowerKey(key);       // key보다 작은 키 중 최대
treeMap.higherKey(key);      // key보다 큰 키 중 최소
```

## Java — Properties (문자열 키-값만, 설정 파일용)
```java
import java.util.Properties;
Properties props = new Properties();
props.setProperty("host", "localhost");
props.getProperty("host");
// 코테에서는 안 씀
```

## 🔥 Map 공통 메소드 (추가 / 검색 / 삭제)

```java
// ✅ 객체 추가
map.put(키, 값);                             // 추가/교체       ← d[k] = v

// ✅ 객체 검색
map.get(키);                                 // 값 가져오기     ← d[k]
map.getOrDefault(키, 기본값);                // 없으면 기본값   ← d.get(k, 기본값)
map.containsKey(키);                         // 키 존재 여부    ← k in d
map.containsValue(값);                       // 값 존재 여부    ← v in d.values()
map.size();                                  // 원소 수         ← len(d)
map.isEmpty();                               // 비었는지        ← not d

// ✅ 객체 삭제
map.remove(키);                              // 키로 삭제       ← del d[k]
map.clear();                                 // 전체 삭제       ← d.clear()

// ✅ 순회
for (String key : map.keySet()) { }          // 키만            ← for k in d
for (int val : map.values()) { }             // 값만            ← for v in d.values()
for (Map.Entry<String, Integer> e : map.entrySet()) {
    e.getKey();   e.getValue();              // 키+값           ← for k,v in d.items()
}

// ✅ defaultdict 패턴 (카운트)
map.put(key, map.getOrDefault(key, 0) + 1);
```

## 💡 대응표
| Python | Java |
|---|---|
| `d = {}` | `HashMap<String, Integer> map = new HashMap<>()` |
| `d[k] = v` | `map.put(k, v)` |
| `d[k]` | `map.get(k)` |
| `d.get(k, 0)` | `map.getOrDefault(k, 0)` |
| `k in d` | `map.containsKey(k)` |
| `v in d.values()` | `map.containsValue(v)` |
| `del d[k]` | `map.remove(k)` |
| `len(d)` | `map.size()` |
| `d.keys()` | `map.keySet()` |
| `d.values()` | `map.values()` |
| `d.items()` | `map.entrySet()` |
| `defaultdict(int)` | `map.getOrDefault(k, 0) + 1` 패턴 |
| `sorted(d.keys())` | `new TreeMap<>(map)` |

## ❗ HashMap vs TreeMap 선택
- **일반적인 키-값 저장** → `HashMap` ← 코테에서 주로 이것
- **키 정렬 필요** → `TreeMap`
- `containsValue()` → O(n)으로 느림, 자주 쓰면 비효율

---

# 🔥 8. Set 컬렉션 → HashSet / TreeSet

> Java Set 컬렉션 2종: `HashSet` (순서 없음, 빠름), `TreeSet` (자동 정렬)

## Python
```python
s = set()
s.add(1)
s.remove(1)
1 in s
a & b   a | b   a - b
```

## Java — HashSet (순서 없음, 중복 제거 ✅ 가장 많이 씀)
```java
import java.util.*;

HashSet<Integer> set = new HashSet<>();
```

## Java — TreeSet (자동 오름차순 정렬, 범위 검색 가능)
```java
TreeSet<Integer> treeSet = new TreeSet<>();
treeSet.first();          // 가장 작은 값  ← min(s)
treeSet.last();           // 가장 큰 값    ← max(s)
treeSet.lower(x);         // x보다 작은 값 중 최대
treeSet.higher(x);        // x보다 큰 값 중 최소
treeSet.headSet(x);       // x 미만인 원소들
treeSet.tailSet(x);       // x 이상인 원소들
```

## 🔥 Set 공통 메소드 (추가 / 검색 / 삭제)

```java
// ✅ 객체 추가
set.add(값);             // 추가 (중복이면 무시)  ← s.add(x)

// ✅ 객체 검색
set.contains(값);        // 포함 여부            ← x in s
set.size();              // 원소 수              ← len(s)
set.isEmpty();           // 비었는지             ← not s

// ✅ 객체 삭제
set.remove(값);          // 값으로 삭제           ← s.remove(x)
set.clear();             // 전체 삭제             ← s.clear()

// ✅ 집합 연산
set1.retainAll(set2);    // 교집합 (set1이 변경됨) ← a & b
set1.addAll(set2);       // 합집합 (set1이 변경됨) ← a | b
set1.removeAll(set2);    // 차집합 (set1이 변경됨) ← a - b

// ✅ 순회
for (int v : set) { }
```

## 💡 대응표
| Python | Java |
|---|---|
| `s = set()` | `HashSet<Integer> set = new HashSet<>()` |
| `s.add(x)` | `set.add(x)` |
| `x in s` | `set.contains(x)` |
| `len(s)` | `set.size()` |
| `s.remove(x)` | `set.remove(x)` |
| `a & b` | `set1.retainAll(set2)` |
| `a \| b` | `set1.addAll(set2)` |
| `a - b` | `set1.removeAll(set2)` |
| `sorted(s)` | `new TreeSet<>(set)` |
| `min(s)` | `treeSet.first()` |
| `max(s)` | `treeSet.last()` |

## ❗ HashSet vs TreeSet
- **중복 제거, 빠른 검색** → `HashSet` ← 코테에서 주로 이것
- **정렬된 상태 유지, 범위 검색** → `TreeSet`
- 집합 연산(retainAll 등)은 원본이 변경됨 → 원본 보존 필요하면 복사 후 사용

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

# 🔥 18. 난수 (Random)

## Python
```python
import random

random.random()           # 0.0 이상 1.0 미만 float
random.randint(1, 10)     # 1 이상 10 이하 int
random.choice([1,2,3])    # 리스트에서 랜덤 선택
random.shuffle(arr)       # 리스트 섞기
```

## Java
```java
// 방법 1: Math.random() — double 타입 난수
double d = Math.random();           // 0.0 이상 1.0 미만 double
int n = (int)(Math.random() * 10); // 0 이상 9 이하 int

// 방법 2: Random 클래스 (더 다양한 기능)
import java.util.Random;

Random rand = new Random();

rand.nextBoolean()        // true 또는 false 랜덤 반환
rand.nextDouble()         // 0.0 이상 1.0 미만 double 반환
rand.nextInt()            // 전체 int 범위 난수
rand.nextInt(n)           // 0 이상 n 미만 int 반환   ← 가장 자주 씀
rand.nextInt(10) + 1      // 1 이상 10 이하 int (범위 조절 패턴)
```

## 💡 대응표
| Python | Java |
|---|---|
| `random.random()` | `Math.random()` 또는 `rand.nextDouble()` |
| `random.randint(1, 10)` | `rand.nextInt(10) + 1` |
| `random.choice(arr)` | `arr[rand.nextInt(arr.length)]` |
| `random.shuffle(arr)` | `Collections.shuffle(list)` |

## ❗ 핵심 규칙
- `Math.random()` → 간단할 때 바로 쓰기
- `Random` 클래스 → `nextBoolean()`, `nextInt(n)` 등 다양한 타입 필요할 때
- `nextInt(n)` 은 **0 이상 n 미만** — 범위 조절할 때 `+ 1` 패턴 기억하기

---

# 🔥 19. 날짜와 시간

> Java 날짜/시간 클래스는 세대가 있다: `Date` (구) → `Calendar` (구) → `LocalDateTime` (신 ✅)

## Python
```python
from datetime import datetime, date, timedelta

now = datetime.now()
now.year   now.month   now.day
now.hour   now.minute  now.second

# 날짜 차이
d1 = date(2024, 1, 1)
d2 = date(2024, 12, 31)
diff = d2 - d1          # timedelta 객체
diff.days               # 364

# 포맷
now.strftime("%Y-%m-%d %H:%M:%S")
```

## Java — Date (구버전, 거의 안 씀)
```java
import java.util.Date;

Date date = new Date();           // 현재 시각
date.getTime();                   // 1970.1.1 기준 밀리초 (타임스탬프)

// ⚠️ 대부분의 메서드가 deprecated — 코테에서는 참고만
```

## Java — Calendar (구버전, 가끔 등장)
```java
import java.util.Calendar;

Calendar cal = Calendar.getInstance();   // 현재 시각

cal.get(Calendar.YEAR)         // 연도
cal.get(Calendar.MONTH)        // 월 (⚠️ 0부터 시작! 1월=0, 12월=11)
cal.get(Calendar.DAY_OF_MONTH) // 일
cal.get(Calendar.HOUR_OF_DAY)  // 시 (24시간)
cal.get(Calendar.MINUTE)       // 분
cal.get(Calendar.SECOND)       // 초
cal.get(Calendar.DAY_OF_WEEK)  // 요일 (1=일요일 ~ 7=토요일)

// 날짜 설정
cal.set(2024, 0, 1);           // 2024년 1월 1일 (월은 0부터!)
cal.set(Calendar.MONTH, 11);   // 12월로 변경

// 날짜 더하기
cal.add(Calendar.DAY_OF_MONTH, 7);   // 7일 후
cal.add(Calendar.MONTH, -1);         // 1달 전

// 날짜 비교
cal1.before(cal2)   // cal1 < cal2?
cal1.after(cal2)    // cal1 > cal2?
```

## Java — LocalDateTime (신버전 ✅ 권장)
```java
import java.time.*;
import java.time.format.DateTimeFormatter;

// 현재 날짜/시간
LocalDateTime now = LocalDateTime.now();
LocalDate today = LocalDate.now();         // 날짜만
LocalTime time = LocalTime.now();          // 시간만

// 값 가져오기
now.getYear()
now.getMonthValue()    // 월 (✅ 1부터 시작! Calendar와 다름)
now.getDayOfMonth()    // 일
now.getHour()
now.getMinute()
now.getSecond()
now.getDayOfWeek()     // MONDAY, TUESDAY ...

// 특정 날짜 생성
LocalDate d = LocalDate.of(2024, 1, 1);
LocalDateTime dt = LocalDateTime.of(2024, 1, 1, 9, 30, 0);

// 날짜 연산
now.plusDays(7)        // 7일 후
now.minusMonths(1)     // 1달 전
now.plusYears(1)       // 1년 후

// 날짜 차이
long days = ChronoUnit.DAYS.between(d1, d2);

// 비교
d1.isBefore(d2)
d1.isAfter(d2)
d1.isEqual(d2)

// 포맷
DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
now.format(fmt)                      // LocalDateTime → 문자열
LocalDateTime.parse("2024-01-01 09:00:00", fmt)  // 문자열 → LocalDateTime
```

## 💡 대응표
| Python | Java |
|---|---|
| `datetime.now()` | `LocalDateTime.now()` |
| `now.year` | `now.getYear()` |
| `now.month` | `now.getMonthValue()` (1부터) |
| `now.day` | `now.getDayOfMonth()` |
| `d2 - d1` | `ChronoUnit.DAYS.between(d1, d2)` |
| `now.strftime(fmt)` | `now.format(DateTimeFormatter.ofPattern(fmt))` |
| `timedelta(days=7)` | `now.plusDays(7)` |

## ❗ 절대 실수하면 안 되는 것

```plaintext
1. Calendar.MONTH는 0부터 시작 → 1월 = 0, 12월 = 11  ← 가장 많이 틀림!
2. LocalDateTime.getMonthValue()는 1부터 시작 → Calendar와 반대!
3. 날짜 연산 결과는 새 객체로 반환 (불변 객체) → 반드시 변수에 받아야 함
   now.plusDays(7);        ❌ now가 바뀌지 않음
   now = now.plusDays(7);  ✅
4. 코테에서 날짜 관련 문제 → LocalDateTime 우선 사용
```

---

# 🚀 핵심 대응표 최종 요약

| 상황 | Python | Java |
|---|---|---|
| 빠른 입력 | `sys.stdin.readline` | `BufferedReader` |
| 가변 배열 | `list` | `ArrayList<Integer>` |
| 앞뒤 삽입/삭제 | `deque` | `LinkedList<Integer>` |
| 정렬된 리스트 | `sorted(list)` | `ArrayList` + `Collections.sort` |
| 딕셔너리 | `dict` | `HashMap<K,V>` |
| 정렬된 딕셔너리 | `sorted(d.keys())` | `TreeMap<K,V>` |
| 집합 | `set` | `HashSet<T>` |
| 정렬된 집합 | `sorted(s)` | `TreeSet<T>` |
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
| 난수 (double) | `random.random()` | `Math.random()` / `rand.nextDouble()` |
| 난수 (int 범위) | `random.randint(1,n)` | `rand.nextInt(n) + 1` |
| 현재 날짜/시간 | `datetime.now()` | `LocalDateTime.now()` |
| 날짜 연산 | `timedelta(days=7)` | `now.plusDays(7)` |
| 날짜 차이 | `(d2-d1).days` | `ChronoUnit.DAYS.between(d1, d2)` |

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
10. Calendar.MONTH는 0부터 시작         (1월 = 0 주의!)
11. LocalDateTime 날짜 연산은 새 객체 반환 → 반드시 변수에 받기
12. nextInt(n)은 0 이상 n 미만          (n 포함 안 됨! +1 패턴 기억)
13. list.remove(1) → 인덱스 1 제거      (값 1 제거하려면 Integer.valueOf(1) 감싸기!)
14. 집합 연산(retainAll 등)은 원본 변경 → 원본 필요하면 복사 후 사용
```

---

# 🔥 최종 한 줄

👉 "구조는 Python과 같다 — 자료구조 클래스 이름과 메서드명만 다르게 바꿔라"