import datetime

def get_days_from_today(date: str) -> int:
    today = datetime.datetime.today()
    date = (datetime.datetime.strptime(date, "%Y-%m-%d"))
    delta = today - date
    
    return delta.days

print(get_days_from_today("2025-10-09"))

