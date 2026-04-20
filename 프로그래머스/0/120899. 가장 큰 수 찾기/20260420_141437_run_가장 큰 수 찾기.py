def solution(array):
    answer = []
    answer.append(max(array))
    
    i = 0
    
    for i in array(i):
        if max(array) == array(i):
            answer.append(i)
        i += 1
            
    return answer