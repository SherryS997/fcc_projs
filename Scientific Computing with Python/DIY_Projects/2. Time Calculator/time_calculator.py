act_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = []
for x in act_days: days.append(x.lower())
periods = ['AM', 'PM']
minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
for x in range(10, 60): minutes.append(str(x))

def add_time(start, duration, day = 'False'):
    to_do = False
    n = 0
    minute = 0
    hour = 0
    start = start.rsplit()
    if day != 'False': to_do = True
    hours = [start[0][:start[0].index(':')], duration[:duration.index(':')]]
    mins = [start[0][(start[0].index(':') + 1):], duration[(duration.index(':') + 1):]]
    for mini in mins: minute += int(mini)
    final_min = minutes[int(minute % 60)]
    for hor in hours: hour += int(hor)
    hour = int((hour + (minute / 60)))
    final_hour = str( hour % 12)
    if final_hour == '0': final_hour = '12'
    if int(hour / 12) % 2 == 0: period = start[1]
    else: 
        if periods.index(start[1]) == 1: period = 'AM'
        else: period = 'PM'
    if start[1] == 'PM' and period != start[1] and hour >= 12: n += 1
    if hour >= 24: n += int(hour / 24)
    if to_do:
        ind = days.index(day.lower()) + n
        if ind > 6: ind = ((ind + 1) % 7) - 1
        day = act_days[ind]
        if n == 0: new_time = final_hour + ':' + final_min + ' ' + period + ',' + ' ' + day
        elif n == 1: new_time = final_hour + ':' + final_min + ' ' + period + ',' + ' ' + day + ' (next day)'
        else: new_time = final_hour + ':' + final_min + ' ' + period + ',' + ' ' + day + ' ' + '(' + str(n) + ' days later)'
    else:
        if n == 0: new_time = final_hour + ':' + final_min + ' ' + period
        elif n == 1: new_time = final_hour + ':' + final_min + ' ' + period + ' (next day)'
        else: new_time = final_hour + ':' + final_min + ' ' + period + ' ' + '(' + str(n) + ' days later)'
    return new_time