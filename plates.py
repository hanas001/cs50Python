import re

def main():
    plate = input("Plate: ").rstrip('\n')
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    two_first_letters_pattern = r'^[a-zA-Z]{2}'
    digit_at_the_end_pattern = r'\d$'
    no_punctuation_marks_pattern = r'^[^\s.,!?]*$'
    interrupted_number_pattern = match = r'\d+[A-Za-z]+\d+'



    if 2 <= len(s) <= 6 and re.search(no_punctuation_marks_pattern, s):
        # print('min and max length test - passed')
        # print('no punctuation marks test - passed')
        if re.match(two_first_letters_pattern, s):
            # print('two first letters test - passed')
            if has_digit(s):
                # print('has digits test - passed')
                if re.search(digit_at_the_end_pattern, s):
                    # print('number at the end test - passed')
                    if not number_starts_with_zero(s):
                        # print('number does not start with zero test - passed')
                        if not re.search(r'\d+[A-Za-z]+\d+', s):
                            # print('number interrupted by a letter test - passed')
                            return True
            else:
                return True
    else:
        return False

def has_digit(string):
    pattern = r'\d'
    match = re.search(pattern, string)
    return bool(match)

def number_starts_with_zero(inp):
    numbers = []
    for n in inp:
        if n.isdigit():
            numbers.append(n)
    # print(numbers)
    if int(numbers[0]) == 0:
        return True


main()