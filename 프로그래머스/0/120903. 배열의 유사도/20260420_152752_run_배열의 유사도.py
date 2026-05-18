def solution(s1, s2):
    
    answer = 0
    for c in s1:
        for d in s2:
            if c == d:
                anwswer += 1       
    return answer