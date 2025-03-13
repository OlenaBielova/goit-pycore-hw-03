import datetime

def get_days_from_today(date: str) -> int:
    today = datetime.datetime.today()
    date = (datetime.datetime.strptime(date, "%Y-%m-%d"))
    delta = today - date
    # print(delta.days)
    return delta.days

get_days_from_today("2023-12-14")

