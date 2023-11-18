from datetime import date
import datetime
import re
import sys
import inflect


class Date:
    def __init__(self, date):
        self.date = date

    def date_splitter(self):
        try:
            date_obj = datetime.datetime.strptime(self.date, '%Y-%m-%d')
            year = date_obj.year
            month = date_obj.month
            day = date_obj.day
            return year, month, day
        except ValueError:
            sys.exit('Invalid date cls')

def main():
    date = input('Date of Birth: ').strip()

    # date = '1970-01-01'
    # date = '2022-11-08'
    # date = '2021-11-08'
    # date = '1986-05-28'
    # date = '1986-28-05'
    # date = 'cat'

    if date_checker(date):
        # print(date)
        date_splitter = Date(date)
        year, month, date = date_splitter.date_splitter()
        # print(year, month, date)


        current_date = datetime.date.today()      #real time
        # current_date = datetime.date(2000, 1, 1)
        # print('Current time', current_date)

        time_delta = current_date - datetime.date(year, month, date)
        # print('Time delta', time_delta)

        total_minutes = int(time_delta.total_seconds() / 60)
        # print('Total minutes', total_minutes)

        # Create an instance of the inflect engine
        p = inflect.engine()

        # Convert the total number of minutes to words
        minutes_in_words = p.number_to_words(total_minutes)
        minutes_in_words = minutes_in_words.replace(' and ', ' ').capitalize()

        # Print the result
        print(minutes_in_words + " minutes")

def date_checker(date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, date):
        # print('Valid')
        return True
    else:
        # print('Invalid')
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()