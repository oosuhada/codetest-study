def solution(angle):
    if 0 < angle and 90 > angle:
        return 1 #예각
    elif angle == 90:
        return 2 #직각
    elif 90 < angle and 180 > angle:
        return 3 #둔각
    elif angle == 180:
        return 4 #평각