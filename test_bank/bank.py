def main():
    while True:
        try:
            greeting = input('Greeting ')
            print('$' + str(value(greeting)))
            break
        except IndexError:
            pass


def value(greeting):
    # print(greeting)
    greeting = greeting.lower().replace(',', '').strip().split()

    if greeting[0] == 'hello':
        change = 0
    elif greeting[0][0] == 'h':
        change = 20
    else:
        change = 100

    return change


if __name__ == "__main__":
    # print(main())
    main()