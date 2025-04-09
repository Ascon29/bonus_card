import datetime


def check_birthday(value):
    date_now = datetime.datetime.today()
    date_birth = datetime.datetime.strptime(str(value), '%Y-%m-%d').replace(year=date_now.year)
    past_date = date_now - datetime.timedelta(days=3)
    future_date = date_now + datetime.timedelta(days=3)
    return future_date.day >= date_birth.day >= past_date.day
