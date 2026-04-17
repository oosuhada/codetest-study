def solution(s):
    answer = ''
    for c in s:
        if s.count(c) == 1 :
            answer += c
    list_answer = list(answer)
    list_answer.sort()
    answer = list_answer.join()
    return answer

# ValueError: not enough values to unpack (expected 2, got 1)
# def solution(s):
#     temp_list = []
#     for c in s:
#         temp_list.append(c)
    
#     for a,b in temp_list:
#         if a == b:
#             temp_list.remove(a,b)
#     answer = ''
#     return temp_list

# ValueError: not enough values to unpack (expected 2, got 1)
# def solution(s):
#     temp_list = []
#     for c in s:
#         temp_list.append(c)
    
#     for a,b in temp_list:
#         if a == b:
#             temp_list.replace('a','')
#             temp_list.replace('b','')

#     return temp_list



# def solution(s):
#     temp_list = []
#     for c in s:
#         temp_list.append(c)
#     answer = ''
    
#     for a in temp_list
#     if temp_list.count(a) > 1:
#         temp_list.replace(a,'')
    
#     return temp_list

# 입력값 〉	"abcabcadc"
# 기댓값 〉	"d"
# 실행 결과 〉	실행한 결괏값 "ababad"이 기댓값 "d"과 다릅니다.
# def solution(s):
#     temp_list = []
#     for c in s:
#         temp_list.append(c)
#     answer = ''
    
#     for a in s:
#         if s.count('a') > 1:
#             temp_list = s.replace(a,'')
    
#     return temp_list
