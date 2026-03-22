def solution(num_list):
    
    #num_list의 홀수만 이어붙인
    odd_list = ""
    #num_list의 짝수만 이어붙인
    even_list = ""
    
    for i in num_list:
        if i % 2 == 1:
            odd_list += str(odd_list(i))
        
        else:
            even_list += str(even_list(i))
        
    answer = int(odd_list) + int(even_list)
    return answer