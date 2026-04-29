def solution(babbling):
    new = []
    for babble in babbling:
        new.append(babble.replace('aya',''))
    answer = 0
    return new


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