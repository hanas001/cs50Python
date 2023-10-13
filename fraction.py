while True:
    try:
        numerator, denominator = list(map(int, input("Fraction: ").split('/')))
        # print('try')
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

# print(str(numerator) + "/" + str(denominator))


def fuel_percentage_to_human(numerator, denominator):
    fuelPercentage = numerator / denominator * 100
    # print('fuel percentage: ', fuelPercentage, '%')

    if fuelPercentage <= 1:
        result = 'E'
    elif 2 <= fuelPercentage <= 98:
        result = str(round(fuelPercentage)) + "%"

    elif 99 <= fuelPercentage <= 100:
        result = "F"

    return result



print(fuel_percentage_to_human(numerator, denominator))