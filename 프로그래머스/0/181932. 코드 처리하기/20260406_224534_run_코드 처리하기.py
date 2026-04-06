def solution(code):
    #초반 생각의 흐름 정리
    #if문, 배열, code[idx] == 1이면 mode change
    #ret = ''
    #mode = 0이고 code[idx] == 1 아닌데 and idx 짝수면 ret += code[idx]
    #mode = 1이고 code[idx] == 1 아닌데 idx 홀수면 ret += code[idx]
    #idx == 0 이라면 return EMPTY 
    
    ref = ''
    mode = 0 #시작할때 mode는 0임
    
    for idx in range(len(code))
    
    if mode == 0:
        if code[idx] == 1:
        mode = 1 - mode
        continue
    
        if idx % 2 == 0:
        ref += code[idx]
        
        else:
        ref += code[idx]
    
    if len(code) == 0
        return "EMPTY"
    
