def solution(lines):
    [[a1, b1], [a2, b2], [a3, b3]] = lines
    start = min(a1,a2,a3,b1,b2,b3)
    end = max(a1,a2,a3,b1,b2,b3)
    array = list(range(start,end))
    new_array = list(range(a1,b1)) + list(range(a2,b2)) + list(range(a3,b3))
    
    answer = 0
    for i in array:
        if new_array.count(i) > 1:
            answer += 1

    return answer

# AttributeError: 'list' object has no attribute 'delete'
# def solution(lines):
#     [[a1, b1], [a2, b2], [a3, b3]] = lines
#     start = min(a1,a2,a3,b1,b2,b3)
#     end = max(a1,a2,a3,b1,b2,b3)
#     array = list(range(start,end+1))
#     new_array = list(range(a1,b1+1)) + list(range(a2,b2+1)) + list(range(a3,b3+1))
#     answer = 0
    
#     for i in array:
#         if i in new_array:
#             new_array.delete(i)
#     return new_array

# AttributeError: 'list' object has no attribute 'delete'
#     for i in array:
#         if i in new_array:
#             new_array.pop(i)
#     return new_array

#   File "/solution.py", line 12
#     new_array.count(i) > 1:
# SyntaxError: invalid syntax
#     answer = 0
#     for i in array:
#         new_array.count(i) > 1:
#             answer += 1
#     return answer

# 테스트 1
# 입력값 〉	[[0, 1], [2, 5], [3, 9]]
# 기댓값 〉	2
# 실행 결과 〉	실행한 결괏값 3이 기댓값 2과 다릅니다.
# 테스트 2
# 입력값 〉	[[-1, 1], [1, 3], [3, 9]]
# 기댓값 〉	0
# 실행 결과 〉	실행한 결괏값 2이 기댓값 0과 다릅니다.
# 테스트 3
# 입력값 〉	[[0, 5], [3, 9], [1, 10]]
# 기댓값 〉	8
# 실행 결과 〉	실행한 결괏값 9이 기댓값 8과 다릅니다.
#     answer = 0
#     for i in array:
#         if new_array.count(i) > 1:
#             answer += 1
#     return answer
# 로직이 틀린 이유: "점"을 세면 안 되는 이유
# 선분의 길이를 구할 때 숫자를 range로 만들어 개수를 세면, 실제 길이보다 1이 더 크게 나오거나, 겹치지 않았는데도 겹쳤다고 판단하는 오류가 발생합니다.

# list(range(start,end+1)) 대신 list(range(start,end))으로 접근하면 점을 세는게 아니라 구간을 세는것이다!