from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_xy(0, 0)
pdf.set_font('helvetica', 'B', 16)
pdf.cell(60)
pdf.cell(75, 10, 'Centered Image', 0, 2, 'C')

# Load image and get its original size
pdf.image('shirtificate/shirtificate.png', x=pdf.w/2-50, y=pdf.h/2-50, w=100, h=100)

pdf.output('test_pdf_with_centered_image.pdf', 'F')