def solution(s):
    temp_list = []
    for c in s:
        temp_list.append(c)
    
    for a,b in temp_list:
        if a == b:
            temp_list.remove(a)
            temp_list.remove(b)
    answer = ''
    return temp_list