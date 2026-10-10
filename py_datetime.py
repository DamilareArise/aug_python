import datetime as dt

tim = dt.datetime.now()
# print(tim)
# print(tim.year)
# print(tim.date())

# print(tim.strftime('%I:%M %p'))
# print(tim.strftime("%d/%m/%Y"))

# future = dt.datetime(2026, 10, 15, 12, 0, 0)
# print(future)

# print(future - tim)

# print(tim + dt.timedelta(hours=2))

user_date = '15/10/25'
# print(type(user_date))
dt_obj = dt.datetime.strptime(user_date, "%d/%m/%y")
# print(dt_obj)

# assignment 
# 1. Print a simple schedule / alarm system

"""
| Code | Meaning                        | Example      |
| ---- | ------------------------------ | ------------ |
| `%Y` | Year (4 digits)                | `2025`       |
| `%y` | Year (2 digits)                | `25`         |
| `%m` | Month (01 to 12)               | `05`         |
| `%B` | Full month name                | `May`        |
| `%b` | Abbreviated month name         | `May`        |
| `%d` | Day of the month (01 to 31)    | `10`         |
| `%H` | Hour (00 to 23)                | `14`         |
| `%I` | Hour (01 to 12)                | `02`         |
| `%p` | AM/PM                          | `PM`         |
| `%M` | Minute (00 to 59)              | `45`         |
| `%S` | Second (00 to 59)              | `09`         |
| `%f` | Microsecond (000000 to 999999) | `123456`     |
| `%z` | UTC offset                     | `+0200`      |
| `%Z` | Time zone name                 | `UTC`, `PST` |
| `%A` | Full weekday name              | `Saturday`   |
| `%a` | Abbreviated weekday name       | `Sat`        |
| `%j` | Day of the year (001 to 366)   | `130`        |
| `%W` | Week number                    |              |

"""
