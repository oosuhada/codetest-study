# 큰 수의 법칙 - page 92

# N M K 
# N 배열의 크기, 
# 주어진 수 M번 더해서 가장 큰수 ,
# 가장 큰 수가 K번까지만 더해질 수 있음
# K는 M보다 작거나 같음

# [ (가장 큰 수 * K번) + (두번째 큰 수 * 1번) ] * M회 반복)

# -------------------------------------------------------------- #

# 1. 문제 목표 정의
# 주어진 숫자들을 M번 더해서 만들 수 있는 "가장 큰 합"을 구해야 한다.

# 2. 가장 큰 값을 만드는 방법
# 합을 크게 만들기 위해서는 당연히 "가장 큰 수"를 최대한 많이 사용하는 것이 유리하다.

# 3. 제약 조건 확인
# 하지만 같은 수는 K번까지만 연속해서 사용할 수 있다.
# → 즉, 가장 큰 수를 무한정 사용할 수 없다.

# 4. 해결 전략 도출
# 가장 큰 수를 K번 사용한 후에는
# 반드시 다른 수(두 번째로 큰 수)를 1번 사용해야 한다.

# 5. 반복 패턴 정의
# 따라서 아래와 같은 구조가 반복된다:

# (가장 큰 수를 K번) + (두 번째로 큰 수를 1번)

# 6. 패턴 길이 정의
# 위 패턴은 총 (K + 1)개의 숫자로 구성된다.

# 7. 전체 반복 횟수 계산
# M번 더해야 하므로,
# 이 패턴이 몇 번 반복되는지 계산한다.

# → 몫: 패턴이 완전히 반복되는 횟수
# → 나머지: 패턴 이후에 남는 횟수

# 8. 각 숫자의 사용 횟수 계산

# 가장 큰 수:
# → (패턴 반복 횟수 * K) + 나머지

# 두 번째로 큰 수:
# → 패턴 반복 횟수

# 9. 최종 합 계산
# (가장 큰 수 * 사용 횟수) + (두 번째 큰 수 * 사용 횟수)

# 10. 결론
# 가장 큰 수를 가능한 한 많이 사용하되,
# K번마다 한 번씩 두 번째 수를 섞는 방식으로 최대값을 만든다.

# -------------------------------------------------------------- #

# 풀이1
# 숫자 개수(n), 총 더하는 횟수(m), 연속 제한(k)
n, m, k = 5, 8, 3

# 숫자 리스트
# numbers는 리스트(list)라는 자료형 → 여러 값을 한 번에 저장하는 배열 같은 것
numbers = [2, 4, 5, 4, 6]  

# sort()는 리스트를 "오름차순(작은 → 큰)"으로 정렬하는 함수
numbers.sort()

# numbers[-1] → 리스트의 "마지막 값"
# → 정렬했기 때문에 가장 큰 값
first = numbers[-1]

# numbers[-2] → 뒤에서 두 번째 값
# → 두 번째로 큰 값
second = numbers[-2]

# 결과를 저장할 변수
result = 0

# 현재까지 "같은 숫자를 연속으로 몇 번 썼는지" 저장하는 변수
count = 0

# range(m) → 0부터 m-1까지 반복
# # 즉, m번 반복하겠다는 의미
for i in range(m):

    # count == k → 연속으로 k번 썼다는 의미
    if count == k:
       
        # += → 기존 값에 더하기
        # result = result + second 와 같은 의미
        result += second

        # 연속 카운트 초기화
        count = 0

    else:
        # 가장 큰 수 더하기
        result += first

        # count = count + 1
        # → 연속 횟수 증가
        count += 1

# print() → 결과 출력
print(result)

# -------------------------------------------------------------- #

# 풀이2 - 반복문 없이 수학적으로 계산하는 방식
# 풀이1은 반복문을 사용해서 매번 조건을 확인하는 방식이었음
n, m, k = 5, 8, 3
numbers = [2, 4, 5, 4, 6]

numbers.sort()

first = numbers[-1]
second = numbers[-2]

# 한 패턴 길이 (예: 6,6,6,5 → 4개)
pattern = k + 1

# // → 몫 (나누기 후 정수 부분만)
# → 패턴이 몇 번 반복되는지
count = m // pattern

# % → 나머지
# → 패턴 반복 후 남은 횟수
remainder = m % pattern

# 가장 큰 수가 총 몇 번 쓰이는지
first_count = count * k + remainder

# 두 번째 수는 패턴마다 1번씩
second_count = count

# 최종 계산
result = first_count * first + second_count * second

# 결과 출력
print(result)

# -------------------------------------------------------------- #

# N, M, K를 공백으로 구분하여 입력받기
# 예: "5 8 3" 이렇게 입력하면
# input() → 문자열 "5 8 3" 로 들어옴
# .split() → 공백 기준으로 나눠서 ["5", "8", "3"] 리스트 생성
# map(int, ...) → 문자열을 정수(int)로 변환
# 최종적으로 n=5, m=8, k=3 이 됨
n, m, k = map(int, input().split())


# 숫자 리스트 입력받기
# 예: "2 4 5 4 6" 입력
# input().split() → ["2", "4", "5", "4", "6"]
# map(int, ...) → [2, 4, 5, 4, 6]
# list(...) → 리스트로 변환
numbers = list(map(int, input().split()))


# 리스트를 오름차순 정렬 (작은 수 → 큰 수)
numbers.sort()


# 가장 큰 수 (리스트의 마지막 값)
first = numbers[-1]

# 두 번째로 큰 수 (뒤에서 두 번째 값)
second = numbers[-2]


# 한 패턴의 길이
# 예: K=3이면 → 6,6,6,5 → 총 4개
pattern = k + 1


# 패턴이 몇 번 반복되는지 (몫)
# 예: m=8, pattern=4 → 8 // 4 = 2
count = m // pattern


# 패턴 반복 후 남는 횟수 (나머지)
# 예: 8 % 4 = 0
remainder = m % pattern


# 가장 큰 수가 더해지는 총 횟수
# (패턴 반복 횟수 * K) + 나머지
# 예: (2 * 3) + 0 = 6
first_count = count * k + remainder


# 두 번째 큰 수가 더해지는 횟수
# 패턴마다 1번씩 등장
# 예: count = 2 → 두 번 등장
second_count = count


# 최종 결과 계산
# (가장 큰 수 * 횟수) + (두 번째 수 * 횟수)
# 예: (6 * 6) + (5 * 2)
result = first_count * first + second_count * second


# 결과 출력
print(result)

# -------------------------------------------------------------- #

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

first = numbers[-1]
second = numbers[-2]

pattern = k + 1
count = m // pattern
remainder = m % pattern

first_count = count * k + remainder
second_count = count

result = first_count * first + second_count * second

print(result)

