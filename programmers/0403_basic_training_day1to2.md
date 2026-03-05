# Python 코딩테스트 학습노트

---

## 풀이한 문제들

---

### 문제 1. 문자열 출력하기

> 문자열 `str`이 주어질 때, `str`을 출력하는 코드를 작성해 보세요.

#### ❌ 오답 기록
```python
str = str(input(HelloWorld!))
str = input(str(HelloWorld!))
str = str(input('HelloWorld!'))  # 실행은 되었음
str = input('HelloWorld!')       # 실행은 되었음
```

#### ✅ 정답
```python
str = input()
print(str)
```

---

### 문제 2. a와 b 출력하기

> 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

#### ❌ 오답 기록
```python
a, b = map(int, input().strip().split(' '))
print('a =' a)
print('b =' b)
```
```python
a, b = map(int, input().strip().split(' '))
print("a =" +a)
print("b =" +b)
```

#### ✅ 정답
```python
a, b = map(int, input().strip().split(' '))
print("a =", a)
print("b =", b)
```

---

### 문제 3. 문자열 반복 출력하기

> 문자열 `str`과 정수 `n`이 주어집니다. `str`이 `n`번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

#### ❌ 오답 기록
- 없음

#### ✅ 정답
```python
print(str * n)
```

---

### 문제 4. 대소문자 바꿔서 출력하기

> 영어 알파벳으로 이루어진 문자열 `str`이 주어집니다. 각 알파벳을 대문자는 소문자로, 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

#### ❌ 오답 기록
- 풀지 못함 → `swapcase()` 코드에 대해 직접 검색함

#### ✅ 정답
```python
print(str.swapcase())
```

---

### 문제 5. 특수문자 출력하기

> 다음과 같이 출력하도록 코드를 작성해 주세요.
> ```
> !@#$%^&*(\'"<>?:;
> ```

#### ❌ 오답 기록
```python
print('!@#$%^&*(\'"<>?:;')
print('!@#$%^&*(\\'"<>?:;')
```

#### ✅ 정답
```python
print('!@#$%^&*(\\'+'\''+'"<>?:;')
```

---

### 문제 6. 덧셈식 출력하기

> 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
> ```
> a + b = c
> ```

#### ❌ 오답 기록
```python
print(a '+' b = a + b)
print(a, '+', b = a + b)
```

#### ✅ 정답
```python
print(a, "+", b, "=", a + b)
# 또는
print(f"{a} + {b} = {a + b}")  # GPT에서 f-string 방식 확인
```

---

### 문제 7. 두 수의 합 출력하기

> 두 개의 문자열 `str1`, `str2`가 공백으로 구분되어 입력으로 주어집니다. `str1`과 `str2`를 이어서 출력하는 코드를 작성해 보세요.

#### ❌ 오답 기록
```python
print(str1, str2)  # 공백이 사이에 들어가서 틀림
```

#### ✅ 정답
```python
print(str1 + str2)
```

---

### 문제 8. 문자열 시계방향 90도 돌리기

> 문자열 `str`이 주어집니다. 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

#### ❌ 오답 기록
- 풀지 못함

#### ✅ 정답
```python
for x in str:
    print(x)
```

---

### 문제 9. 짝수 홀수 구분하기

> 자연수 n이 입력으로 주어졌을 때, n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

#### ❌ 오답 기록
```python
a = int(input())
if a%2 == 0    # 콜론(:) 누락
    print(a 'is even')
    else print(a 'is odd')  # else 들여쓰기 잘못됨
```

#### ✅ 정답
```python
a = int(input())
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")
```

---

### 문제 10. 문자열 일부 교체하기

> 문자열 `my_string`, `overwrite_string`과 정수 `s`가 주어집니다. `my_string`의 인덱스 `s`부터 `overwrite_string`의 길이만큼을 `overwrite_string`으로 바꾼 문자열을 return 하는 `solution` 함수를 작성해 주세요.

#### ❌ 오답 기록
```python
def solution(my_string, overwrite_string, s):
    answer = ''
    return answer
```

#### ✅ 정답 (GPT 해석 참고)
```python
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    return answer
```

---

## 📚 공부한 내용

---

### 공부 1. `print()`에서 콤마(,) vs f-string 원리 정리

---

#### 1️⃣ 콤마(,) 방식

`print()`는 여러 값을 쉼표로 구분해서 넣으면 자동으로 문자열 변환 + **공백**을 사이에 넣어서 출력한다.

```python
a, b = 4, 5

print(a, "+", b, "=", a + b)
# 내부 동작 개념:
# print(str(a) + " " + "+" + " " + str(b) + " " + "=" + " " + str(a+b))

# 출력: 4 + 5 = 9
```

**핵심 특징**
- 자동 형변환 (int → str)
- 기본 구분자: 공백(`" "`)
- 빠르고 안전해서 코딩테스트에 적합

**`sep` 옵션으로 구분자 변경 가능**
```python
print(a, "+", b, "=", a + b, sep="")
# 출력: 4+5=9
```

---

#### 2️⃣ f-string 방식

문자열 안에 변수를 직접 넣는 방식 (Python 3.6 이상)  
`{}` 안에 변수나 연산식을 넣으면 결과가 문자열로 변환되어 들어간다.

```python
a, b = 4, 5

print(f"{a} + {b} = {a + b}")
# 출력: 4 + 5 = 9
```

**핵심 특징**
- `{}` 안에서 계산 가능
- 가독성이 매우 좋음
- 실무에서 가장 많이 사용

**다양한 활용 예시**
```python
name = "Gabriel"
age = 30

print(f"이름: {name}, 나이: {age}")
# 출력: 이름: Gabriel, 나이: 30

print(f"{a} + {b} = {a + b}, 두 수의 곱은 {a * b}")
# 출력: 4 + 5 = 9, 두 수의 곱은 20
```

---

#### 🔍 콤마 vs f-string 차이 비교

| 방식 | 코드 | 출력 |
|------|------|------|
| 콤마 | `print(a, b)` | `4 5` (공백 자동 삽입) |
| f-string | `print(f"{a}{b}")` | `45` (공백 없음) |
| 콤마 + sep | `print(a, b, sep=", ")` | `4, 5` |

---

#### ⚠️ 자주 하는 실수

```python
# ❌ 문자열 + 숫자 직접 더하기 → TypeError 발생
print("a = " + a)

# ✅ 해결 방법 1: 콤마
print("a =", a)

# ✅ 해결 방법 2: f-string
print(f"a = {a}")
```

---

#### 🧭 언제 무엇을 써야 할까?

| 상황 | 추천 방식 |
|------|-----------|
| 코딩 테스트 | 콤마 방식 (빠르고 실수 적음) |
| 실무 / 가독성 중요 | f-string |

---

### 공부 2. 문자열 처리 핵심 패턴 정리

> 📌 문자열은 **immutable(변경 불가)**이다.  
> 직접 수정이 불가능하므로 → **슬라이싱 + 이어붙이기**로 처리해야 한다.

---

#### 1️⃣ 문자열 슬라이싱 기본 개념

```python
# 문자열[start:end]
# → start부터 end "직전까지" 잘라냄

s = "abcdef"

print(s[0:3])  # "abc"
print(s[:3])   # "abc" (start 생략 = 0)
print(s[3:])   # "def" (end 생략 = 끝까지)
```

---

#### 2️⃣ 문자열 삽입 (중간에 끼워넣기)

```python
# 패턴: str[:i] + new + str[i:]

s = "abcdef"
new = "ZZZ"
i = 3

result = s[:i] + new + s[i:]
print(result)  # "abcZZZdef"

# s[:3] → "abc"
# s[3:] → "def"
# 사이에 new 삽입
```

---

#### 3️⃣ 문자열 삭제 (일부 구간 제거)

```python
# 패턴: str[:i] + str[i+k:]

s = "abcdef"
i = 2   # 시작 위치
k = 3   # 삭제 길이

result = s[:i] + s[i+k:]
print(result)  # "abf"

# "cde" 제거됨
```

---

#### 4️⃣ 문자열 교체 ⭐ (코테 단골)

```python
# 패턴: str[:i] + replace + str[i+len(replace):]

s = "abcdef"
replace = "ZZZ"
i = 2

result = s[:i] + replace + s[i+len(replace):]
print(result)  # "abZZZf"

# 기존 "cde" → "ZZZ"로 교체
```

---

#### 5️⃣ len() 함수 (길이 구하기)

```python
s = "hello"
print(len(s))  # 5
```

---

#### 6️⃣ 문자열 반복 처리 (for문)

```python
# 한 글자씩 처리할 때 사용

s = "abc"

for c in s:
    print(c)

# 출력:
# a
# b
# c
```

---

#### 📌 핵심 요약

| 패턴 | 코드 |
|------|------|
| 슬라이싱 | `str[start:end]` |
| 삽입 | `str[:i] + new + str[i:]` |
| 삭제 | `str[:i] + str[i+k:]` |
| 교체 | `str[:i] + replace + str[i+len(replace):]` |

> 🔑 **핵심 원칙**: 문자열은 수정 불가 → 항상 **잘라서 붙인다**