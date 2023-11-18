from fpdf import FPDF
from PIL import Image


name = input('Name: ')
# name = 'Evgeny Golubenko'

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()

# Load image and get its original size
img = Image.open("shirtificate.png")
pdf.image(img, x=pdf.w/2-100, y=pdf.h/2-100, w=200, h=200)

# text block 1
pdf.set_font('helvetica', size=48)
text = "CS50 Shirtificate"
text_width = pdf.get_string_width(text)
# print('CS50 Shirtificate width', text_width)
pdf.text((pdf.w - text_width) / 2, pdf.y + 20, text)

# text block 2
pdf.set_font('helvetica', size=22)
text = f"{name} took CS50"
text_width = pdf.get_string_width(text)
# print('... took cs50 width', text_width)
# pdf.set_text_color(0, 0, 0)
pdf.set_text_color(255, 255, 255)
pdf.text((pdf.w - text_width) / 2, pdf.h/2 - 30, text)


pdf.output("shirtificate.pdf")