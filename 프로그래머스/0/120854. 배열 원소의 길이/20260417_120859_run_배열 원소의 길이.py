def solution(strlist):
    
    #list 안에 string의 길이를 계산
    #이중 구조는 map을 사용해야 할지 간단하게 구하는 함수 있을지
    answer = []
    for c in strlist:
        answer.append (len(c))

    return answer