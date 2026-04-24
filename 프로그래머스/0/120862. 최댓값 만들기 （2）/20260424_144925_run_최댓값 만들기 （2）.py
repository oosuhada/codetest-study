def solution(numbers):
    leng = len(numbers)
    new_list = []
    
    for c in numbers:
        new_list.append(abs(c))
    new_list.sort()
    
    return new_list[leng-2] * new_list[leng-1]