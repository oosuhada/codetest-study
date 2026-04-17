def solution(sides):
    # a = max(sides)
    sides.sort()
    if sides[2] <= sides[0] +sides[1]:
        return 2
    else:
        return 1