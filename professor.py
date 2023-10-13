import random


def main():
    level = get_level()
    # print(level)
    # generated_integer = generate_integer(level)
    # print('this is generated integer', generated_integer)
    score = 0

    #ten math problems to solve
    for _ in range(10):
        generated_integer_one = generate_integer(level)
        generated_integer_two = generate_integer(level)
        print(generated_integer_one, "+", generated_integer_two, "=", end=' ')
        math_problem = generated_integer_one + generated_integer_two

        # user input is checked whether it is an int and not a word
        while True:
            try:
                guess = int(input())
                break
            except ValueError:
                print('EEE')
                print(generated_integer_one, "+", generated_integer_two, "=", end=' ')
                pass

        #check if the guess it right
        if guess == math_problem:
            score += 1
        else:
            # loop three times to receive correct answer
            for _ in range(2):
                print('EEE')
                print(generated_integer_one, "+", generated_integer_two, "=", end=' ')

                # user input is checked whether it is an int and not a word
                while True:
                    try:
                        guess = int(input())
                        break
                    except ValueError:
                        print('EEE')
                        print(generated_integer_one, "+", generated_integer_two, "=", end=' ')
                        pass
                pass
            print(generated_integer_one, "+", generated_integer_two, "=", math_problem)

    print('Score: ', score)



def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            game_level = int(input('Level: '))
            if game_level in levels:
                return game_level
                break
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        rand_number = random.randint(0, 9)
    elif level == 2:
        rand_number = random.randint(10, 99)
    elif level == 3:
        rand_number = random.randint(100, 999)
    return rand_number

def user_guess():
    while True:
        try:
            guess = int(input())
            return guess
        except ValueError:
            print('EEE')
            pass


if __name__ == "__main__":
    main()