def solution(n):
    
    answer = 0
    
    # 1부터 n까지 반복
    for i in range(1, n+1):
        
        if n % 2 == 1:
            if i % 2 == 1:
                answer += i  # 🔴 수정: 들여쓰기 부족 → 반드시 if 안에 들어가야 함
        
        else:  # 🔴 수정: else 뒤에 콜론(:) 빠짐
            if i % 2 == 0:
                answer += i * i  # 🔴 수정: 들여쓰기 부족 → if 안에 포함
    
    return answer