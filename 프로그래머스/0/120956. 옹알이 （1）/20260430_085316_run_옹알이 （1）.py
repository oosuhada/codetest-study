def solution(babbling):
    new = []
    for babble in babbling:
        babbling = babble.replace('aya','')
        babbling = babble.replace('woo','')
    return babbling
    answer = 0



# def solution(babbling):
#     for babble in babbling:
#         babble.replace("aya","")
#         babble.replace("ye","")
#         babble.replace("woo","")
#         babble.replace("ma","")
#     answer = 0
#     return babbling

# 실행한 결괏값 ["aya","yee","u","maa","wyeoo"]이 기댓값 1과 다릅니다.
# aya 가 왜 repalce 되지 않았는지 이해하지 못함
# def solution(babbling):
#     for babble in babbling:
#         babble.replace('aya','')
#     answer = 0
#     return babbling

# def solution(babbling):
#     babbling2 = babbling[:]
#     for babble in babbling2:
#         babble.replace('aya','')
#     answer = 0
#     return babbling2

# def solution(babbling):
#     new = []
#     for babble in babbling:
#         new.append(babble.replace('aya',''))
#         new.append(babble.replace('woo',''))
#     answer = 0
#     return new
