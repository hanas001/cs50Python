grocery_list = []

while True:
    try:
        item = input().upper()
        # print(item)
        grocery_list.append(item)

    except EOFError:
        break

# print(grocery_list)

grocery_set = sorted(set(grocery_list))
# print(grocery_set)

for item in grocery_set:
    print(grocery_list.count(item), end=' ')
    print(item)