import re
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# 9/8/1636
# September 8, 1636
# 23/6/1912
# December 80, 1980
# 9 / 8 / 1636

pattern_digits = r"^\d{1,2}\/\d{1,2}\/\d{4}$"
pattern_word = r"^[a-zA-Z]+\s\d{1,2},\s\d{4}$"

while True:
    raw_data = input('Date: ').strip()
    if re.findall(pattern_digits, raw_data):
        # print('digits')
        month, date, year = raw_data.split('/')

        if int(month) in range(1, 13) and int(date) in range(1, 32):

            print(year, end='-')
            print(f"{int(month):02}", end='-')
            print(f"{int(date):02}")

            break
        else:
            pass

    elif re.findall(pattern_word, raw_data):
        # print('text month')
        month_date , year = raw_data.split (',')
        month, date = month_date.split(' ')
        month = month.title ()

        if month in months and int(date) in range(1, 32):

            print(int(year), end='-')
            print ( f"{months.index ( month ) + 1:02}", end='-')
            print(f"{int(date):02}")

            break
        else:
            pass
    else:
        pass