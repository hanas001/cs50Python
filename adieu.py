name_list = []

while True:
    try:
        user_input = input()
        name_list.append(user_input)
    except EOFError:
        break

# print(name_list)
sentence = "Adieu, adieu, to "
combined_names = ''

number_names = len(name_list)

if number_names == 1:
    print(sentence + name_list[0])
elif number_names == 2:
    print(sentence + name_list[0] + ' and ' + name_list[-1])
elif number_names > 2:
    # print('three names or more received')
    combined_names += name_list[0]
    for name in name_list[1:-1]:
        combined_names += ', ' + name
    combined_names += ', and ' + name_list[-1]
    print(sentence + combined_names)