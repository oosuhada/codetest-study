def solution(ineq, eq, n, m):
    
    # >, =
    if ineq == ">" and eq == "=":
        if n >= m:
            return 1
    
    # 🔴 수정: or → elif 로 변경 (조건을 이어서 검사)
    elif ineq == "<" and eq == "=":
        if n <= m:
            return 1
    
    # 🔴 수정: or → elif
    elif ineq == ">" and eq == "!":
        if n > m:
            return 1
    
    # 🔴 수정: or → elif
    elif ineq == "<" and eq == "!":
        if n < m:
            return 1
    
    # 🔴 수정: else 뒤에 콜론 추가
    else:
        return 0
