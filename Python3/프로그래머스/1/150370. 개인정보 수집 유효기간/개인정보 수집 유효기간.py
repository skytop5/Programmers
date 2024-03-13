def solution(today, terms, privacies):
    terms_date = {}
    for term in terms:
        terms_date[term[0]] = int(term[2:])
        
    today = list(map(int, today.split('.')))
    
    check = []
    cnt = 1
    
    for i in privacies:
        spl = i.split(" ")
        pri_date = list(map(int,spl[0].split('.')))
        pri_date[1] += terms_date[spl[1]]
        
        if pri_date[1] > 12:
            if pri_date[1] % 12 == 0:
                pri_date[0] += (pri_date[1] // 12) - 1
                pri_date[1] = 12
            else:
                pri_date[0] += pri_date[1] // 12
                pri_date[1] %= 12
        
        
        if today[0] > pri_date[0]:
            check.append(cnt)
        elif today[0] == pri_date[0] and today[1] > pri_date[1]:
            check.append(cnt)
        elif today[0] == pri_date[0] and today[1] == pri_date[1] and today[2] > pri_date[2] - 1:
            check.append(cnt)
        cnt += 1
        
    return check