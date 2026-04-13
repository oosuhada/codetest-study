#     # list_letter = list(letter)
#     letter1 = letter
    
#     letter1 = letter1.replace('.-','a')
#     letter1 = letter1.replace('-...','b')
#     letter1 = letter1.replace('-.-.','c')
#     letter1 = letter1.replace('-..','d')
#     letter1 = letter1.replace('.','e')
#     letter1 = letter1.replace('..-.','f')
#     letter1 = letter1.replace('--.','g')
#     letter1 = letter1.replace('....','h')
#     letter1 = letter1.replace('..','i')
#     letter1 = letter1.replace('.---','j')
#     letter1 = letter1.replace('-.-','k')
#     letter1 = letter1.replace('.-..','l')
#     letter1 = letter1.replace('--','m')
#     letter1 = letter1.replace('-.','n')
#     letter1 = letter1.replace('---','o')
#     letter1 = letter1.replace('.--.','p')
#     letter1 = letter1.replace('--.-','q')
#     letter1 = letter1.replace('.-.','r')
#     letter1 = letter1.replace('...','s')
#     letter1 = letter1.replace('-','t')
#     letter1 = letter1.replace('..-','u')
#     letter1 = letter1.replace('...-','v')
#     letter1 = letter1.replace('.--','w')
#     letter1 = letter1.replace('-..-','x')
#     letter1 = letter1.replace('-.--','y')
#     letter1 = letter1.replace('--..','z')
    
#     return letter1

# morse = { 
#     '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#     '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#     '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#     '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#     '-.--':'y','--..':'z'
# }

# 모르던 개념
# letter1.replace('.-','a') -> 변환된 문자열을 반환만 하고, letter1 자체는 바뀌지 않음
# letter1 = letter1.replace('.-','a') -> 결과값을 다시 넣어줘야 함

# 실행한 결괏값 "eeee e aee aee mt"이 기댓값 "hello"과 다릅니다.
# 모스부호는 공백 단위로 나눠야 한다 지금 방식은 전체 문자열에서 '.', '-'를 계속 바꾸는 구조라서 겹침 문제가 발생함

# 딕셔너리 방식으로 풀이 - 새로 알게된 개념
def solution(letter):
    
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    # 1. 공백 기준으로 모스부호 분리
    letter_list = letter.split(' ')  # ['....', '.', '.-..', '.-..', '---']
    
    # 2. 변환 결과 저장할 변수
    answer = ''
    
    # 3. 하나씩 변환
    for code in letter_list:
        answer += morse[code]  # 딕셔너리로 바로 변환
    
    return answer


# 파이썬스럽게 더 줄인 풀이
# def solution(letter):
#     morse = { 
#         '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#         '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#         '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#         '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#         '-.--':'y','--..':'z'
#     }
#     return ''.join(morse[i] for i in letter.split())