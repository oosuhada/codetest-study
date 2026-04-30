def solution(numlist, n):
    for x in numlist:
        key = (abs(x-n), -x)
    answer = []
    return key




#어떻게 접근해야할지 감도 안잡혀서

### 핵심 개념 3 — `sorted()`의 `key` 파라미터

# - 기본: `sorted(arr)`
# - 내림차순: `sorted(arr, reverse=True)`
# - 길이 기준: `sorted(words, key=len)`
# - 복합 기준(튜플): `sorted(numbers, key=lambda x: (abs(x-n), -x))`

# ```python
# numbers = [1, 2, 3, 4, 5, 6]
# n = 4
# result = sorted(numbers, key=lambda x: (abs(x - n), -x))
# ```

# ```python
# def solution(numlist, n):
#     def key_func(x):
#         return (abs(x - n), -x)
    
#     return sorted(numlist, key=key_func)
# ```

# - Lamda식이란?

# ```python
# # 일반 함수
# def 두배(x):
#     return x * 2

# # lambda (완전히 동일)
# 두배 = lambda x: x * 2

# lambda  x  :  x * 2
#          ↑       ↑
#        입력    반환값
# ```

# - **튜플 `(a, b)` 정렬은 `a` 먼저 비교, 같으면 `b` 비교**

# ```python
# (1, -5)  vs  (1, -3)
#  ↑  ↑         ↑  ↑
# 같음 -5 < -3 이므로 (1,-5)가 먼저

# -x 를 쓰는 이유는 오름차순 정렬에서 큰 수를 앞에 오게 하는 트릭
# sorted(numbers, key=lambda x: (abs(x - n), -x))
# ```

# - 기본 `sorted()`의  `key` 사용

# ```python
# words = ["banana", "apple", "kiwi", "fig"]

# sorted(words)           # → ['apple', 'banana', 'fig', 'kiwi']  (알파벳순)
# sorted(words, key=len)  # → ['fig', 'kiwi', 'apple', 'banana'] (길이순)
# ```