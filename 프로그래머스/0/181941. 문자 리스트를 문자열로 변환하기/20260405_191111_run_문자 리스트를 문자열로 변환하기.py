def solution(arr):
    
    answer = ''  # 결과 문자열 초기화
    
    for ch in arr:  # 배열의 각 요소 순회
        answer += ch  # 하나씩 붙이기
    
    return answer