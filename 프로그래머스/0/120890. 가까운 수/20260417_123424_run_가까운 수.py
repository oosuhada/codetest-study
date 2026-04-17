def solution(array, n):
    
    new_array = array
    new_array.append(n)
    new_array.sort()
    
    for i in new_array():
        if new_array(i) == n:
            return new_array(i-1)