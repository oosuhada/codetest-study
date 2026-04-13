def solution(numbers):
    answer = 0
    total_content = 0
    total_index = 0
    
    for c in numbers:
        total_content += c
    for i in range(len(numbers)+1):
        total_index += i
    answer = (total_content / total_index)
    
    return answer