import calendar
def solution(a, b):
    days = ["MON","TUE","WED","THU","FRI","SAT", "SUN"]
    dayNumber = calendar.weekday(2016, a, b)
    return days[dayNumber]