def solution(ineq, eq, n, m):
    
    def solution(ineq, eq, n, m):
    
    # >, =
    if ineq == ">" and eq == "=":
        if n >= m:
            return 1
    
    # <, =
    or ineq == "<" and eq == "=":
        if n <= m:
            return 1
    
    # >, !
    or ineq == ">" and eq == "!":
        if n > m:
            return 1
    
    # <, !
    or ineq == "<" and eq == "!":
        if n < m:
            return 1
    else
        return 0 
