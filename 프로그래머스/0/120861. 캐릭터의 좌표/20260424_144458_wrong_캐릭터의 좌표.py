def solution(keyinput, board):
    x = 0
    y = 0
    answer = [x, y]
    
    n, m = board
    a = -(n//2)
    b = (n//2)
    for z in keyinput:
        if z == "left":
            x -= 1
        elif z == "right":
            x += 1
        elif z == "down":
            y -= 1
        elif z == "up":
            y += 1
    return a+b


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
        