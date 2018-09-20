import datetime


WEDNESDAY = 2
SATURDAY = 5

DRAW_DATES = [
    WEDNESDAY,
    SATURDAY
]

DRAW_TIME = datetime.time(20, 0, 0, 0)


def eval_next_draw(date=None):
    if date is None:
        date = datetime.datetime.now()

    time = date.time()
    weekday = date.weekday()

    if weekday in DRAW_DATES and time < DRAW_TIME:
        days = 0
    elif weekday < WEDNESDAY:
        days = WEDNESDAY - weekday
    elif weekday >= WEDNESDAY and weekday < SATURDAY:
        days = SATURDAY - weekday
    else:
        days = WEDNESDAY - weekday + 7

    next_draw = date + datetime.timedelta(days=days)
    return next_draw.replace(hour=20, minute=0, second=0, microsecond=0)
