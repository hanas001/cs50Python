import sys
from tabulate import tabulate
import csv

try:
    arg = sys.argv[1:]
except IndexError:
    sys.exit('Too few command-line arguments')

if len(arg) == 0:
    sys.exit('Too few command-line arguments')
elif len(arg) > 1:
    sys.exit('Too many command-line arguments')
elif len(arg) == 1:
    full_name = str(arg[0])
    try:
        file_name, extension = full_name.split('.')
        if extension == 'csv':
            try:
                with open(full_name) as csvfile:
                    reader = csv.reader(csvfile)
                    # print(reader)
                    table = []
                    header = []
                    columns = 0
                    for row in reader:
                        if columns == 0:
                            for _ in row:
                                header.append(_)
                            columns += 1
                        else:
                            table.append(row)
                        # print(row)

                    print(tabulate(table, headers=header, tablefmt="grid"))

            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a CSV file')
    except ValueError:
        sys.exit('Not a CSV file')