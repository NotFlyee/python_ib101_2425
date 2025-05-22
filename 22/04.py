import datetime
system_date = datetime.date(2019, 9, 1)
delta_date = datetime.timedelta(days=int(input()))
birthday_date = system_date + delta_date
print(birthday_date.day, birthday_date.month)
