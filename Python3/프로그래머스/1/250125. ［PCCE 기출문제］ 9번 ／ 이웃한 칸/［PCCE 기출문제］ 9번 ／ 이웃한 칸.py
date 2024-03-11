def solution(board, h, w):
    n = len(board)
    count = 0
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if (n > h_check >= 0) and (n > w_check >= 0):
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count