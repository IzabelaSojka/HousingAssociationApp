import datetime


def deltaTime(date):
    now = datetime.date.today()
    delta = date - now
    return delta.days