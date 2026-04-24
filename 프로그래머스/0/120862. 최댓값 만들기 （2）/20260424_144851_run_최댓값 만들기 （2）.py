def solution(numbers):
    leng = len(numbers)
    new_list = []
    
    for c in numbers:
        new_list.append(abs(c))
    new_list.sort()
    
    
    answer = 0
    return new_list