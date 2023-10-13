amount_due = 50
change_owed = 0
total_coins = 0

accepted_coins = [5, 10, 25]

while total_coins < 50:
    coins = input('Insert coin: ')
    try:
        coins = int(coins)
    except ValueError:
        print(f'Amount Due: {amount_due}')
        continue

    if coins in accepted_coins:
        total_coins += coins
        amount_due -= coins
        if amount_due > 0:
            print(f'Amount Due: {amount_due}')
        else:
            break
    else:
        print(f'Amount Due: {amount_due}')


change_owed = 50 - total_coins
print(f'Change Owed: {abs(change_owed)}')