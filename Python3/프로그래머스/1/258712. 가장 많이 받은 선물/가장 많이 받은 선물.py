def solution(friends, gifts):
    cnt = [[0] * len(friends) for _ in range(len(friends))] 
    
    for i in gifts:
        j = i.split()
        cnt[friends.index(j[0])][friends.index(j[1])] += 1
    
    score = []
    for i in range(len(friends)):
        x = 0
        for j in range(len(friends)):
            x += cnt[j][i]
        score.append(sum(cnt[i]) - x)
        
    next = [0 for _ in range(len(friends))]
    for i in range(len(cnt)):
        for j in range(len(cnt[i])):
            if cnt[i][j] > 0 and cnt[i][j] > cnt[j][i]:
                next[i] += 1
            elif cnt[i][j] == cnt[j][i]:
                if score[i] > score[j]:
                    next[i] += 1
    return max(next)