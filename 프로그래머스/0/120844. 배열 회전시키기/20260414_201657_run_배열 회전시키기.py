def solution(numbers, direction):
    answer = []
    n = len(numbers)
    
    if direction == "right":
        answer[0] = numbers[n-1]
        for i in numbers[i]:
            answer[i+1] = numbers[i]
    
    elif direction == "left":
        answer[n-1] = numbers[0]
        for i in numbers[i]:
            answer[i] = numbers[i+1]

    return answer