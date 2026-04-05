def solution(str1, str2):
    
    answer = ''  # 결과를 저장할 문자열
    
    for i in range(len(str1)):  # 문자열 길이만큼 반복
        answer += str1[i]  # str1에서 하나 추가
        answer += str2[i]  # str2에서 하나 추가
    
    return answer