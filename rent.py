from datetime import datetime
import datecalc

HOLIDAYS = [
    datetime(2020, 1, 1),
    datetime(2020, 1, 2),
    datetime(2020, 4, 10),
    datetime(2020, 5, 8),
    datetime(2020, 5, 25),
    datetime(2020, 8, 3),
    datetime(2020, 11, 30),
    datetime(2020, 12, 25),
    datetime(2020, 12, 28),
]

print 'Rent due:'
for payday in datecalc.getDays(24, HOLIDAYS):
    print payday.strftime('%a %d %b %Y')


