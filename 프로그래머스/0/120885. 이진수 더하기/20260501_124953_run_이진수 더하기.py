def solution(bin1, bin2):
    answer = 0
    a = format(10, bin1)
    b = format(10, bin2)
    return a

# TypeError: 'str' object cannot be interpreted as an integer
# def solution(bin1, bin2):
#     answer = bin(format(10, bin1) + format(10, bin2))
#     return answer

# TypeError: format() argument 2 must be str, not int
# def solution(bin1, bin2):
#     answer = bin(format(10, int(bin1)) + format(10, int(bin2)))
#     return answer


# bin, format 개념 몰랐음. 알면 더 쉽게 풀리겠지만 기억 안나는 경우를 대비해서 방법2도 연습 필요

# 방법1.10진수 -> 2진수 변환 (숫자, 문자열 -> "0b101")
# bin(숫자): 숫자를 2진수 문자열로 변환합니다. 앞에 '0b'가 붙습니다.
# print(bin(10)) # 출력: '0b1010'

# format(숫자, 'b'): '0b' 없이 2진수 문자열만 가져옵니다.
# print(format(10, 'b')) # 출력: '1010'

# 방법2.
# 1. 10진수를 2진수 문자열로 만들기10진수 숫자를 2로 계속 나누면서 발생하는 나머지를 거꾸로 이어 붙이면 2진수가 됩니다.반복문 사용: 숫자가 0이 될 때까지 2로 나눈 나머지를 결과 문자열의 앞에 추가합니다.몫 업데이트: 숫자를 2로 나눈 몫으로 계속 갱신합니다.pythondef decimal_to_binary(n):
#     if n == 0: return "0"
#     result = ""
#     while n > 0:
#         result = str(n % 2) + result  # 나머지를 앞에 붙임
#         n //= 2                       # 몫을 다음 계산에 사용
#     return result

# print(decimal_to_binary(10))  # 출력: "1010"
# Use code with caution.2. 2진수 문자열을 10진수 숫자로 바꾸기2진수의 각 자릿수에 2의 거듭제곱을 곱해서 모두 더하면 10진수가 됩니다.원리: 오른쪽 끝 자리부터 \(2^{0}\), \(2^{1}\), \(2^2 \dots\) 순서대로 가중치를 곱합니다.pythondef binary_to_decimal(binary_str):
#     decimal = 0
#     power = 0
#     # 문자열을 뒤집어서 오른쪽(작은 자리)부터 계산
#     for digit in reversed(binary_str):
#         if digit == '1':
#             decimal += (2 ** power)
#         power += 1
#     return decimal

# print(binary_to_decimal("1010"))  # 출력: 10
# Use code with caution.