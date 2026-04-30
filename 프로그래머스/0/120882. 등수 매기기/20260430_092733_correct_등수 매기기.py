def solution(score):
    #영어 수학 평균점수를 먼저 계산
    avg = []
    for eng, math in score:
        avg.append((eng+math)/2)
    #리스트 내 평균 점수보다 더 큰 점수 개수 + 1
    rank = []
    for s in avg:
        rank_calc = sum(1 for x in avg if x > s) + 1
        rank.append(rank_calc)
    return rank

#rank_calc = sum(1 for x in avg if x > s) + 1 이 수식 제대로 이해하지 못함