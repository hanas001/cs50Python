def main():
    tweet = input('Input: ')
    print(shorten(tweet))


def shorten(word):

    vowel_list = ["a", "e", "i", "o", 'u']
    twttr_str = ''

    for i in word:
        if i.lower() not in vowel_list:
            twttr_str += i
    return twttr_str

if __name__ == "__main__":
    main()