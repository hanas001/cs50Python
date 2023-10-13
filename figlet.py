import sys
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 3:
    # print(' length test - passed')
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        # print('-f and --font test - passed')
        if sys.argv[2] in font_list:
            # print('font in font list test - passed')
            font = sys.argv[2]
            figlet.setFont(font=font)
        else:
            print('Invalid usage')
            sys.exit(1)
    else:
        print('Invalid usage')
        sys.exit(1)
elif 1 < len(sys.argv) <= 2:
    print('Invalid usage')
    sys.exit(1)

phrase = input('Input: ')

figlet_phrase = figlet.renderText(phrase)
print(figlet_phrase)