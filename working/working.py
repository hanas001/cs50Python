import re
import sys


def main():
    # print(convert(input("Hours: ")))
    # hours = '9 AM to 5 PM'
    # hours = '9:00 AM to 5:00 PM'
    # hours = '10 PM to 8 AM'
    # hours = '10:30 PM to 8:50 AM'
    # hours = '9:60 AM to 5:60 PM'
    # hours = '9 AM - 5 PM'
    # hours = '09:00 AM - 17:00 PM'
    # hours = '12 AM to 12 PM' #00:00 to 12:00
    # hours = '12:00 AM to 12:00 PM' #00:00 to 12:00
    # print(convert(hours))

    print(convert(input("Hours: ")))

def convert(s):
    regex = re.compile(r'\b((\d{1,2}):?(\d{2})?\s+(AM|PM)\s+to\s+(\d{1,2}):?(\d{2})?\s+(AM|PM))\b')
    matcher = regex.search(s)

    if matcher:
        start, end = s.split('to')
        start = start.strip()
        end = end.strip()
        # print(f'{start} to {end}')

        start01, start02 = start.split(' ')
        # print(f'{start01} {start02}')
        if start02 == 'AM':
            # print(start01)
            if not ':' in start01:
                start01_24 = int(start01)
                if start01_24 >= 12:
                    start01_24 = start01_24 % 12
                start01_24 = f'{start01_24:02}' + ':' + '00'
            else:
                start01_24_h, start01_24_m = start01.split(':')
                start01_24_h, start01_24_m = int(start01_24_h), int(start01_24_m)
                if start01_24_h >= 12:
                    start01_24_h = start01_24_h % 12
                if start01_24_m > 59:
                    raise ValueError
                # print(start01_24_h, start01_24_m)
                # print(type(start01_24_h))
                start01_24 = f'{start01_24_h:02}' + ':' + f'{start01_24_m:02}'
                # print('>>>>>>', start01_24)
        elif start02 == 'PM':
            if not ':' in start01:
                start01_24 = int(start01) + 12
                start01_24 = f'{start01_24:02}' + ':' + '00'
            else:
                start01_24_h, start01_24_m = start01.split(':')
                start01_24_h, start01_24_m = int(start01_24_h) + 12, int(start01_24_m)
                if start01_24_m > 59:
                    raise ValueError
                start01_24 = f'{start01_24_h:02}' + ':' + f'{start01_24_m:02}'
                # print('>>>>>>', start01_24)


        # print(type(start01_24))
        # print(f'{start01_24:02}')
        # start01_24 = f'{start01_24:02}'

        end01, end02 = end.split(' ')
        # print(f'{end01} {end02}')
        if end02 == 'AM':
            if not ':' in end01:
                end01_24 = int(end01)
                end01_24 = f'{end01_24:02}' + ':' + '00'
            else:
                end01_24_h, end01_24_m = end01.split(':')
                end01_24_h, end01_24_m = int(end01_24_h), int(end01_24_m)
                end01_24 = f'{end01_24_h:02}' + ':' + f'{end01_24_m:02}'

        elif end02 == 'PM':
            if not ':' in end01:
                if not int(end01) >= 12:
                    end01_24 = int(end01) + 12
                else:
                    end01_24 = int(end01)
                end01_24 = f'{end01_24:02}' + ':' + '00'
        # print(f'{end01_24:02}')
        # end01_24 = f'{end01_24:02}'
            else:
                end01_24_h, end01_24_m = end01.split(':')
                end01_24_h, end01_24_m = int(end01_24_h), int(end01_24_m)
                if not int(end01_24_h) >= 12:
                    end01_24_h = int(end01_24_h) + 12
                else:
                    end01_24_h = int(end01_24_h)
                end01_24 = f'{end01_24_h:02}' + ':' + f'{end01_24_m:02}'

        time24 = start01_24 + ' to ' + end01_24
        return time24

        # return True

    else:
        raise ValueError


if __name__ == "__main__":
    main()