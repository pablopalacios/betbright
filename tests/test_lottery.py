import datetime

from freezegun import freeze_time

from betbright.lottery import eval_next_draw


def test_eval_next_draw_returns_next_wednesday():
    dates = [
        # Saturday, after draw
        datetime.datetime(2018, 9, 15, 20, 0, 0, 1),
        # Sunday
        datetime.datetime(2018, 9, 16),
        # Monday
        datetime.datetime(2018, 9, 17),
        # Tuesday
        datetime.datetime(2018, 9, 18),
        # Wednesday, before draw
        datetime.datetime(2018, 9, 19, 19, 59, 59),
    ]
    expected = datetime.datetime(2018, 9, 19, 20, 0, 0, 0)
    for date in dates:
        observed = eval_next_draw(date)
        assert observed == expected


def test_eval_next_draw_returns_next_saturday():
    dates = [
        # Saturday, before draw
        datetime.datetime(2018, 9, 22, 19, 59, 59),
        # Wednesday, after draw
        datetime.datetime(2018, 9, 19, 20, 0, 0, 1),
        # Thusday
        datetime.datetime(2018, 9, 20),
        # Friday
        datetime.datetime(2018, 9, 21),
    ]
    expected = datetime.datetime(2018, 9, 22, 20, 0, 0, 0)
    for date in dates:
        observed = eval_next_draw(date)
        assert observed == expected


@freeze_time('2018-9-19 20:30:30')
def test_can_eval_next_draw_without_arguments():
    expected = datetime.datetime(2018, 9, 22, 20)
    observed = eval_next_draw()
    assert observed == expected
