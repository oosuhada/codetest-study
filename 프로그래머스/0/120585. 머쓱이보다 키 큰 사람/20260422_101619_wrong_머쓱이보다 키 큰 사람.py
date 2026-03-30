def solution(array, height):
    new_array = array
    new_array.append(height)
    new_array.sort()
    leng = len(array)
    answer_i = 0
    
    for c in new_array:
        if c == height:
            answer_i = new_array.index(c)
    
    answer = leng - (answer_i + 1)
    
    return answer

# AttributeError: 'list' object has no attribute 'array'
# def solution(array, height):
#     new_array = array
#     new_array.append(height)
#     new_array2 = new_array.sort(): or new_array2 = new_array.sorted():
    
#     answer = 0
#     return new_array2

# 테스트 1 〉	실패 (0.00ms, 9.02MB)
# 테스트 2 〉	실패 (0.00ms, 9.24MB)
# 테스트 3 〉	통과 (0.00ms, 9.13MB)
# 테스트 4 〉	실패 (0.02ms, 9.22MB)
# def solution(array, height):
#     new_array = array
#     new_array.append(height)
#     new_array.sort()
#     leng = len(array)
#     answer_i = 0
    
#     for c in new_array:
#         if c == height:
#             answer_i = new_array.index(c)
    
#     answer = leng - answer_i - 1
    
#     return answer

# 입력값 〉	[149, 180, 192, 170], 167
# 기댓값 〉	3
# 실행 결과 〉	실행한 결괏값 [5,1]이 기댓값 3과 다릅니다.
# 입력값 〉	[180, 120, 140], 190
# 기댓값 〉	0
# 실행 결과 〉	실행한 결괏값 [4,3]이 기댓값 0과 다릅니다.
# def solution(array, height):
#     new_array = array
#     new_array.append(height)
#     new_array.sort()
#     leng = len(array)
#     answer_i = 0
    
#     for c in new_array:
#         if c == height:
#             answer_i = new_array.index(c)
    
#     answer = (leng + 1) - (answer_i + 1)
    
#     return [leng, answer_i]