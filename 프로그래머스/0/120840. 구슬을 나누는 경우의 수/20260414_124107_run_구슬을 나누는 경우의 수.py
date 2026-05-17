def solution(balls, share):
    #경우의 수. balls 중에 share 만큼 고르는 경우의 수
    
    answer = balls! / ((balls - share)! * share!)
    return answer