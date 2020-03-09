from datetime import datetime
from dateutil.relativedelta import relativedelta

SATURDAY = 5
SUNDAY = 6

def getDays(dayOfMonth, holidays):
    today = datetime.today()
    monthsLeftInYear = 12 - (today.month - 1)
    for i in range(monthsLeftInYear): 
        day = datetime(today.year, today.month, dayOfMonth) + relativedelta(months=i)
        while day.weekday() == SATURDAY or day.weekday() == SUNDAY or day in holidays:
            day -= relativedelta(days=1)
        yield day
