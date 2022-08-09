import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
all_fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        f = sys.argv[2]
        if f in all_fonts:
            figlet.setFont(font=f)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    figlet.setFont(font=random.choice(all_fonts))
else:
    sys.exit("Invalid usage")

s = input("Input: ")
print(figlet.renderText(s))
