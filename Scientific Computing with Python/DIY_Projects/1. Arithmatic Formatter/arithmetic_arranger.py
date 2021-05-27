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


def arithmetic_arranger(problems, binary = None):
    arranged_problems = 'Cum'

    return arranged_problems