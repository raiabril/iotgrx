import datetime


def format_date(date):
    cur = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    if cur.hour == 0 or cur.hour == 1:
        return datetime.datetime.strftime(cur, format="%d %b %H:%M")
    else:
        return datetime.datetime.strftime(cur, format="%H:%M")


def get_color(value):
    greenFill = "rgba(151,220,150,0.2)"
    greenLine = "rgba(73,193,71,1)"
    yellowFill = "rgba(245,240,50,0.2)"
    yellowLine = "rgba(240,245,50,1)"
    redFill = "rgba(234,121,106,0.2)"
    redLine = "rgba(210,50,28,1)"

    if value > 3000:
        return redFill, redLine
    elif value > 2000:
        return yellowFill, yellowLine
    else:
        return greenFill, greenLine
