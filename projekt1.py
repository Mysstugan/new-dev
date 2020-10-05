import datetime
from datetime import date
from dateutil import relativedelta

today = date.today()
today2 = today.strftime("%B %d, %Y")
now = datetime.datetime.now()
last_month = now.month-1 if now.month > 1 else 12
last_year = now.year - 1
nextmonth = datetime.date.today() + relativedelta.relativedelta(months=1)


print(f"Today is: {today}")
print(today2)
print(last_month)
print(last_year)
print(nextmonth)

