def main():
    while True:
        try:
            numerator, denominator = list(map(int, input("Fraction: ").split('/')))
            # print(numerator)
            # print(type(numerator))

            if denominator < numerator:
                pass
            else:
                break
        except (ValueError):
            # print('ValueError')
            pass
        except (TypeError):
            # print('TypeError')
            pass

    fraction = str(numerator) + '/' + str(denominator)
    # print(type(fraction))

    print(gauge(convert(fraction)))
    # print(type(convert(fraction)))
    # print(type(gauge(convert(fraction))))


def convert(fraction: str) -> int:
    x, y = map(int, fraction.split('/'))

    if x > y or y <= 0 or x < 0:
        raise ValueError
    percentage = round(x / y * 100)
    return percentage


def gauge(percentage):
    if 0 <= percentage <= 1:
        result = 'E'
    elif 2 <= percentage <= 98:
        result = str(percentage) + "%"
    elif 99 <= percentage <= 100:
        result = "F"
    else:
        raise ValueError
    return result


if __name__ == "__main__":
    main()