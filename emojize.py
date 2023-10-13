import emoji

text_line = input().strip()

emoji_line = emoji.emojize(text_line, language='alias')

print(emoji_line, end='')