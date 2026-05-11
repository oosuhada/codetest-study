def solution(rsp):
    #to win rsp
    #when rsp is 2, answer is 0
    #when rsp is 0, answer is 5
    #when rsp is 5, answer is 2
    
    #rsp.replace()방식으로 수정하면 이미 변환된 값 함께 변환됨
    #dictionary 방식?
    
    replace_map = {"2":"0", "0":"5", "5":"2"}
    
    answer = [replace_map.get(n, n) for n in rsp]
    return answer

# # 리스트 값을 딕셔너리 기준으로 일괄 변환
# replace_map = {1: 'one', 2: 'two', 3: 'three'}
# nums = [1, 2, 3, 1, 2]

# result = [replace_map.get(n, n) for n in nums]
# # ['one', 'two', 'three', 'one', 'two']
# #  없는 값은 get(n, n)으로 원본 유지