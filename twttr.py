tweet = input('Input: ')
vowel_list = ["a", "e", "i", "o", 'u']
twttr_str = ''

for i in tweet:
    if i.lower() not in vowel_list:
        twttr_str += i

print('Output: ', twttr_str)