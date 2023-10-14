import re


def main():
    plate = input("Plate: ").rstrip('\n').rstrip(' ')
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    two_first_letters_pattern = r'^[a-zA-Z]{2}'
    digit_at_the_end_pattern = r'\d$'
    no_punctuation_marks_pattern = r'^[^\s.,!?]*$'
    alphabetical_pattern = r'^([^A-Za-z])'
    has_digit_pattern = r'\d'
    number_interrupted_by_letter_patter = r'\d+[A-Za-z]+\d+'



    if 2 <= len(s) <= 6 and re.search(no_punctuation_marks_pattern, s):
        # print('min and max length test - passed', end=' ')
        # print('no punctuation marks test - passed')


            if re.match(two_first_letters_pattern, s):
                # print('two first letters test - passed')

                #plate has digit test
                match = re.search(has_digit_pattern, s)
                if bool(match):
                    # print('has digits test - passed')

                    if re.search(digit_at_the_end_pattern, s):
                        # print('number at the end test - passed')

                        #number starts with zero check
                        numbers = []
                        number_starts_with_zero = False
                        for n in s:
                            if n.isdigit():
                                numbers.append(n)
                        if int(numbers[0]) == 0:
                            number_starts_with_zero = True

                        if not number_starts_with_zero:
                            # print('number does not start with zero test - passed')
                            if not re.search(number_interrupted_by_letter_patter, s):
                                # print('number interrupted by a letter test - passed')
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return True
            else:
                return False

    else:
        return False


if __name__ == "__main__":
    main()