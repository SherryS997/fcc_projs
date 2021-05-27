pp = ["32 + 658", "1 - 3801", "45 + 66", "123 + 49"]


def calculator(list):
    ans = []
    for dd in list:
        cc = dd.rsplit()
        if cc[1] == '+': nn = int(cc[0]) + int(cc[2])
        else: nn = int(cc[0]) - int(cc[2])
        ans.append(nn)
    return ans

def is_error(list):
    if len(list) > 5: return True
    for dd in list:
        cc = dd.rsplit()
        if len(cc) == 3:
            if cc[1] != '+' and cc[1] != '-': return True
            elif not cc[0].isdecimal() or not cc[2].isdecimal(): return True
            elif len(cc[0]) > 4 or len(cc[2]) > 4: return True
        else: return True
    return False


def error(list):
    ans = None
    if len(list) > 5:
        ans = 'Error: Too many problems.'
        return ans
    for dd in list:
        cc = dd.rsplit()
        if len(cc) == 3:
            if cc[1] != '+' and cc[1] != '-':
                ans = "Error: Operator must be '+' or '-'."
                return ans
            elif not cc[0].isdecimal() or not cc[2].isdecimal():
                ans = 'Error: Numbers must only contain digits.'
                return ans
            elif len(cc[0]) > 4 or len(cc[2]) > 4:
                ans = 'Error: Numbers cannot be more than four digits.'
                return ans
        else:
            ans = 'Other issues'
            return ans
    return None


print(error(pp))