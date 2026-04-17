def solution(cipher, code):
    list_cipher = list(cipher)
    
    answer_list = []
    n = len(list_cipher)
    i = 0
    
    #for i in list_cipher(i):
    while i < n:
        if (i+1) % code == 0:
            answer_list.append(list_cipher(i))
        i += 1

        
    
    
    return answer_list