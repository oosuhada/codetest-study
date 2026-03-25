def solution(numbers):
    answer = 0
    total_content = 0
    total_index = 0
    
    for c in numbers:
        total_content += c
        total_index = len(numbers)
    answer = (total_content / total_index)
    
    return answer