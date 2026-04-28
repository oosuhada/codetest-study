def solution(babbling):
    new = []
    for babble in babbling:
        babble = babble.replace('aya','')
        babble = babble.replace('ye','')
        babble = babble.replace('woo','')
        babble = babble.replace('ma','')
    answer = 0
    return babbling


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

#막힌 부분 - replace로 4개 여러개를 replace해서 저장하는 방법 모르겠음
# 문제 1: replace()는 원본을 바꾸지 않아요
# pythonbabble.replace('aya', '')  # ❌ 결과를 버림
# babble = babble.replace('aya', '')  # ✅ 변수에 재할당해야 함
# Python 문자열은 불변(immutable) 이라 replace()는 새 문자열을 반환할 뿐, 원본은 그대로예요.

# 문제 2: 여러 개를 replace할 때 체이닝하면 돼요
# pythonbabble = babble.replace('aya', '').replace('ye', '').replace('woo', '').replace('ma', '')

# 문제 3: "최대 1번만" 조건
# 문제에서 이미 각 발음은 최대 1번만 등장한다고 보장해줘요.
# 그래서 replace()가 전부 교체해도 실제로는 최대 1번만 교체돼서 괜찮아요.