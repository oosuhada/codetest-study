def solution(score):
    rank = []
    for eng, math in score:
        rank.append((eng+math)/2)
    answer = []
    return rank