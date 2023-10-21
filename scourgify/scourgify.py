import sys
import csv

try:
    arg = sys.argv[1:]
except IndexError:
    sys.exit('Too few command-line arguments')


if len(arg) < 2:
    sys.exit('Too few command-line arguments')
elif len(arg) > 2:
    sys.exit('Too many command-line arguments')
elif len(arg) == 2:
    full_name_in = str( arg[0 ] )
    full_name_out = str(arg[-1])
    try:
        file_name_in, extension_in = full_name_in.split( '.' )
        file_name_out , extension_out = full_name_out.split ( '.' )
        if extension_in == 'csv' or extension_out == 'csv':

            with open(str(full_name_out), 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['first', 'last', 'house'])
                csvfile.close()
                # csvwriter.writerow('')
            try:
                with open( full_name_in ) as csv_file:
                    reader = csv.DictReader(csv_file)
                    # print(reader)
                    table = []
                    for row in reader:
                        last_name, first_name = row['name'].split(',')
                        first_name = first_name.strip(' ')

                        with open(str(full_name_out), 'a') as csvfile:
                            # Create a CSV writer object
                            csvwriter = csv.DictWriter(csvfile, fieldnames=['first', 'last', 'house'])

                            # Write the data to the CSV file
                            csvwriter.writerow({'first': first_name,
                                                 'last': last_name,
                                                 'house': row['house']
                                                 })
                            csvfile.close()


                    # print(table)
                    # sys.exit(f'Table written to {full_name_out} file successfully!')
                    # sys.exit()
                    # break

            except FileNotFoundError:
                sys.exit(f'Could not read {full_name_in} or {full_name_out}')
        else:
            sys.exit('Not a CSV file')
    except ValueError:
        sys.exit('Not a CSV file')