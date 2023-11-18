import re
import sys


def main():
    print(count(input("Text: ")))
    text = 'um'
    # text = 'um?'
    # text = 'Um, thanks for the album.'
    # text = 'Um, thanks, um...'
    # print(count(text))


def count(s):
    pattern = r'\bum\b'
    #pattern = r'^um\b'
    regex = re.compile(pattern, re.IGNORECASE)
    matches = regex.findall(s)
    # print(matches)
    return len(matches)


if __name__ == "__main__":
    main()