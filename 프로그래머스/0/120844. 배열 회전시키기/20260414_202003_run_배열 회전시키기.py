def solution(numbers, direction):
    answer = []
    n = len(numbers)
    i = 0
    
    if direction == "right":
        answer[0] = numbers[n-1]
        while i < n:
            for i in numbers[i]:
                answer[i+1] = numbers[i]
                i += 1
    
    elif direction == "left":
        answer[n-1] = numbers[0]
        while i < n:
            for i in numbers[i]:
                answer[i] = numbers[i+1]
                i += 1

    return answer

#IndexError: list assignment index out of range