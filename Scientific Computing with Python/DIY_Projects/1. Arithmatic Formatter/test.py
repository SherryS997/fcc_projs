pp = ["32 - 658", "1 - 3801", "45 + 43", "123 + 49"]


def calculator(list):
    ans = []
    for dd in list:
        nn = 0
        cc = dd.rsplit()
        if cc[1] == '+':
            nn = int(cc[0]) + int(cc[2])
        else:
            nn = int(cc[0]) - int(cc[2])
        ans.append(nn)
    return ans

print(calculator(pp))

