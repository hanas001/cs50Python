import re

def is_valid(s):
    regex = r'^([^A-Za-z])'
    match = re.match(regex, s)
    return bool(match)

if __name__ == "__main__":
    plate = input("Plate: ").rstrip('\n').rstrip(' ')
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")