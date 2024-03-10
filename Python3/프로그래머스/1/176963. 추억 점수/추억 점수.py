def solution(name, yearning, photo):
    y = []
    for i in photo:
        z = 0
        for x in i:
            if x in name:
                z += yearning[name.index(x)]
        y.append(z)
    return y