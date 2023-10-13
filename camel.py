def main():
    phrase = input('camelCase: ')
    snake_case(phrase)


def snake_case(phrase):
    snake_case = ''
    for i in phrase:
        if i.isupper():
            snake_case += "_" + i.lower()
        else:
            snake_case += i
    print('snake_case: ', snake_case)
    return snake_case
main()