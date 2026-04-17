def solution(cipher, code):
    list_cipher = list(cipher)
    
    i = 0
    answer_list = []
    for i in list_cipher(i):
        if (i+1) % code == 0:
            answer_list.append(i)
    
    
    
    return answer_list