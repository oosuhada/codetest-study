def solution(n):
    answer = []
    for c in range[0:n+1]:
        if n % c == 0:
            answer.append(c)
    return answer