def solution(cipher, code):
    list_cipher = list(cipher)
    
    answer_list = []
    n = len(list_cipher)
    i = 0
    answer = ''
    #for i in list_cipher(i):
    while i < n:
        if (i+1) % code == 0:
            answer_list.append(i)
        i += 1
    
    for 'c' in answer_list:
        answer.append(list_cipher(c))

    return answer