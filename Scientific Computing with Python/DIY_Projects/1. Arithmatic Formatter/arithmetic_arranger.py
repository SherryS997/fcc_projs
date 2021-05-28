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
    if len(list) > 5: ans = 'Error: Too many problems.'
    else:
        for dd in list:
            cc = dd.rsplit()
            if len(cc) == 3:
                if cc[1] != '+' and cc[1] != '-': ans = "Error: Operator must be '+' or '-'."
                elif not cc[0].isdecimal() or not cc[2].isdecimal(): ans = 'Error: Numbers must only contain digits.'
                elif len(cc[0]) > 4 or len(cc[2]) > 4: ans = 'Error: Numbers cannot be more than four digits.'
            else: ans = 'Other issues'
    return ans


def calculator(list):
    ans = []
    for dd in list:
        cc = dd.rsplit()
        if cc[1] == '+': nn = int(cc[0]) + int(cc[2])
        else: nn = int(cc[0]) - int(cc[2])
        ans.append(nn)
    return ans


def arithmetic_arranger(problems, to_solve = False):
    arranged_problems = ''
    req = []
    if is_error(problems): return error(problems)
    if to_solve: ans = calculator(problems)
    for problem in problems:
        dd = problem.rsplit()
        if len(dd[0]) > len(dd[2]):
            spaces = (len(dd[0]) + 1) - len(dd[2])
            dd[0] = (' ' * 2) + dd[0]
            dd[1] = dd[1] + (' ' * spaces) + dd[2]
            dd[2] = '-' * len(dd[0])
            if to_solve == True:
                this_ans = str(ans[problems.index(problem)])
                this_ans = (' ' * (len(dd[0]) - len(this_ans))) + this_ans
                dd.append(this_ans)
        else:
            spaces = (len(dd[2]) + 2) - len(dd[0])
            dd[0] = (' ' * spaces) + dd[0]
            dd[1] = dd[1] + ' ' + dd[2]
            dd[2] = '-' * len(dd[0])
            if to_solve == True:
                this_ans = str(ans[problems.index(problem)])
                this_ans = (' ' * (len(dd[0]) - len(this_ans))) + this_ans
                dd.append(this_ans)
        for char in dd: req.append(char)
    if to_solve: aa = len(problems)
    else: aa = 3
    for x in range(aa):
        y = x
        while y < len(req):
            word = req[y]
            if to_solve: y += 4
            else: y += 3
            arranged_problems += word
            if y < len(req): arranged_problems += ' ' * 4
        if x < (aa - 1): arranged_problems += '\n'
    return arranged_problems