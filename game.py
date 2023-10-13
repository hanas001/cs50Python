import random

# range of numbers
while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            break
    except Exception:
        pass
# print('random range', level)

rand_number = random.randint(1, level)
# print('random number in a range ', rand_number)

#user's guess
def guess_me():
    while True:
        guess = (input('Guess:'))
        try:
            guess = int(guess)
            if guess > 0:
                return guess
                break
            elif guess <= 0:
                pass
        except Exception:
            pass


while True:
    # print('inside loop')
    user_guess = guess_me()

    if user_guess > rand_number:
        print('Too large!')
        pass
    elif user_guess < rand_number:
        print('Too small!')
        pass
    else:
        print('Just right!', end='')
        break