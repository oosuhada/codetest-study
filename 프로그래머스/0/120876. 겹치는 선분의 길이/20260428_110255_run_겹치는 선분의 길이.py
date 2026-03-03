def solution(lines):
    [[a1, b1], [a2, b2], [a3, b3]] = lines
    start = min(a1,a2,a3,b1,b2,b3)
    end = max(a1,a2,a3,b1,b2,b3)
    array = list(range(start,end+1))
    new_array = list(range(a1,b1+1)) + list(range(a2,b2+1)) + list(range(a3,b3+1))
    answer = 0
    
    for i in array:
        if i in new_array:
            new_array.delete(i)
    return new_array