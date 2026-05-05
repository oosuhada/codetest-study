def solution(keyinput, board):
    x = 0
    y = 0
    answer = [x, y]
    
    n, m = board
    a = -(n//2)
    b = (n//2)
    c = -(m//2)
    d = (m//2)
    
    for z in keyinput:
        if z == "left" and x > a:
            x -= 1
        elif z == "right" and x < b:
            x += 1
        elif z == "down" and y > c:
            y -= 1
        elif z == "up" and y < d:
            y += 1
    return [x, y]


# def solution(keyinput, board):
#     a = 0
#     b = 0
#     answer = [a, b]
#     d, e = board
#     while a <= d and b <= e:
#         for c in keyinput:
#             if c == "left":
#                 a -= 1
#             elif c == "right":
#                 a += 1
#             elif c == "down":
#                 b -= 1
#             elif c == "up":
#                 b += 1
#         return answer

#     for c in keyinput:
#         while a <= d and b <= e: 이것도 시도해봄
        