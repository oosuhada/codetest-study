def solution(keyinput, board):
    answer = [a, b]
    d, e = board
    for c in keyinput:
        while a <= d and b <= e:
            if c == "left":
                a -= 1
            elif c == "right":
                a += 1
            elif c == "down":
                b -= 1
            elif c == "up":
                b += 1
    return answer