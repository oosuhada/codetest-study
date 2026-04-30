def solution(babbling):
    answer = 0
    new = []
    for babble in babbling:
        babble = babble.replace('aya',' ')
        babble = babble.replace('ye',' ')
        babble = babble.replace('woo',' ')
        babble = babble.replace('ma',' ')
        if babble == "":
            answer += 1
    return answer


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

# def solution(babbling):
#     new = []
#     for babble in babbling:
#         babble = babble.replace('aya','')
#         babble = babble.replace('ye','')
#         babble = babble.replace('woo','')
#         babble = babble.replace('ma','')
#     answer = 0
#     return babbling 이렇게 풀었을때 〉    실행한 결괏값 ["aya","yee","u","maa","wyeoo"]이 기댓값 1과 다릅니다. 이렇게 교체가 안되고 그대로 출력되는 이유 모르겠음
# 이유: babble은 babbling 내부와 연결이 끊어진 별도 변수예요
# pythonfor babble in babbling:
#     babble = babble.replace('aya', '')  # babble이라는 새 변수에 저장
#                                         # babbling[0]은 그대로!
# for babble in babbling 할 때 babble은 리스트 원소의 복사본이에요.
# babble = babble.replace(...) 로 재할당하면 babble 변수만 바뀌고, 원본 babbling 리스트는 전혀 안 바뀌어요.

# 그림으로 보면
# babbling = ["aya", "yee", ...]
#                ↑
#            babble = "aya"   ← for문에서 복사
#            babble = ""      ← replace 후 재할당
               
# babbling = ["aya", "yee", ...]  ← 원본은 그대로!
# babble이 ""이 됐어도 babbling[0]은 여전히 "aya"

# 해결법: 리스트 원본을 수정하거나, 결과를 따로 모아야 해요
# 방법 1: 인덱스로 직접 수정
# pythonfor i in range(len(babbling)):
#     babbling[i] = babbling[i].replace('aya', '')
#     # 이렇게 하면 리스트 원본이 바뀜
# 방법 2: 결과를 새 리스트에 저장 (권장)
# pythonfor babble in babbling:
#     babble = babble.replace('aya', '').replace('ye', '').replace('woo', '').replace('ma', '')
#     if babble == '':
#         answer += 1
# babbling을 굳이 수정할 필요 없이, 빈 문자열인지 바로 확인하면 돼요!

# 입력값 〉	["aya", "yee", "u", "maa", "wyeoo"]
# 기댓값 〉	1
# 실행 결과 〉	실행한 결괏값 2이 기댓값 1과 다릅니다.
# def solution(babbling):
#     answer = 0
#     new = []
#     for babble in babbling:
#         babble = babble.replace('aya','')
#         babble = babble.replace('ye','')
#         babble = babble.replace('woo','')
#         babble = babble.replace('ma','')
#         if babble == "":
#             answer += 1
#     return answer
# 핵심 문제
# "wyeoo"는 w + ye + oo 이지, woo 를 발음하는 게 아니에요.
# 근데 ye를 먼저 지우니까 "wyeoo" → "woo"가 되고, 그 다음 woo까지 지워져서 통과해버리는 거예요.