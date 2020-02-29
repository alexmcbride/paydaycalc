from datetime import datetime
import datecalc

HOLIDAYS = [
    datetime(2020, 1, 1),
    datetime(2020, 3, 17),
    datetime(2020, 4, 10),
    datetime(2020, 4, 13),
    datetime(2020, 5, 4),
    datetime(2020, 5, 8),
    datetime(2020, 5, 25),
    datetime(2020, 6, 1),
    datetime(2020, 6, 13),
    datetime(2020, 8, 3),
    datetime(2020, 8, 31),
    datetime(2020, 12, 25),
    datetime(2020, 12, 18)
]

print 'Paydays:'
for payday in datecalc.getDays(26, HOLIDAYS):
    print payday.strftime('%a %d %b %Y')
