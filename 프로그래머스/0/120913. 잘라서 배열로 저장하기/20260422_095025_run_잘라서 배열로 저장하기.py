def solution(my_str, n):
    leng = len(my_str)
    x = leng // str(n)
    answer = []
    
    for i in range(1,x):
        answer.append(my_str[0,i*n+1])
    answer.append(my_str[x*n+1:leng+1])
    
    return answer