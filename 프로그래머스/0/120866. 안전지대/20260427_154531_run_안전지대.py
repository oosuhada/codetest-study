def solution(board):
    n = len(board)
    new_board = board
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            new_board[ni][nj] = 2
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if new_board[i][j] == 0:
                answer += 1
    
    return answer


# 5x5 배열 
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0]
# [0, 0, 0, 0, 0]

# (3,2) 지뢰 -> 위험지역 
# (2,1) (2,2) (2,3)
# (3,1) (3,3)
# (4,1) (4,2) (4,3)

# 5x5 배열
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 1, 1, 0]
# [0, 0, 0, 0, 0]

# (3, 2), (3, 3) 지뢰 -> 위험지역 
# (2,1) (2,2) (2,3) (2,4)
# (3,1) (3,4)
# (4,1) (4,2) (4,3) (4,4)

#기존 지뢰 매설 지역은 그대로1, 지뢰 매설 지역은 2로 치환, 나머지 0의 개수 구하기

#gpt에서 2중 for문으로 board[i][j] == 1인 지뢰 위치 (i, j) 찾기 힌트 얻음
# def solution(board):
#     n = len(board)
    
#     for i in range(n):        # 행
#         for j in range(n):    # 열
#             print(i, j, board[i][j])