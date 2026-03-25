def solution(a, b, c):
    answer = 0
    
    # 🔴 [개념 1] a == b == c
    # 👉 Python에서는 이렇게 "연속 비교" 가능
    # 👉 (a == b) and (b == c) 와 동일
    
    if a == b == c:
        # 🔴 [실수 1] × 사용 → Python에서는 * 사용해야 함
        # ❌ (a + b + c) × (...)
        # ✅ (a + b + c) * (...)
        
        answer = (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
    
    # 🔴 두 개만 같은 경우
    elif a == b or b == c or a == c:
        answer = (a + b + c) * (a*a + b*b + c*c)
    
    # 🔴 [실수 2] elif 잘못 사용 + 비교연산자 없음
    # ❌ elif answer = a + b + c
    # 👉 elif는 "조건"이 들어가야 함
    
    # 🔴 세 개 다 다른 경우는 그냥 else로 처리
    else:
        answer = a + b + c # 반드시 들여쓰기
    
    return answer