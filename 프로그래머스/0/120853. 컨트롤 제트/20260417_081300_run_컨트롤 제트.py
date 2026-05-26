def solution(s):
    #Z의 index를 먼저 찾자!
    Z_list = []
    i = 0
    n = len(s)
    
    #for i in s[i]:
    while i < n:
        if s[i] == "Z":
            Z_list.append(i)
            i += 1
    
            
    answer = 0
    return Z_list