import sys

try:
    arg = sys.argv[1:]
except IndexError:
    sys.exit('Too few command-line arguments')


# print(arg)
# print(len(arg))

if len(arg) == 0:
  sys.exit('Too few command-line arguments')
elif len(arg) == 1:
    file_name, extension = arg[0].split( '.' )
    full_name = f"{file_name}.{extension}"
    # print(full_name)
    line_counter = 0
    if extension == 'py':
        try:
            with open(full_name) as lines:
                for line in lines:
                    line = line.lstrip()
                    if not line.startswith('#') and len(line) > 0:
                        line_counter += 1
        except FileNotFoundError:
            sys.exit('File does not exist')
    else:
        sys.exit('Not a Python file')

elif len(arg) > 1:
    sys.exit('Too many command-line arguments')

print(line_counter, end='')