from fpdf import FPDF


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# title
pdf.set_font("Arial", "B", 16)
pdf.cell(txt="CS50 shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.cell(h=15, txt=" ", new_x="LMARGIN", new_y="NEXT", align="X")

# shirt
pdf.image("shirtificate.png", w=pdf.epw)

# writing
shirt_text = input("Name: ")
pdf.set_font_size = 70
pdf.set_text_color(255, 255, 255)
pdf.text(x=70, y=100, txt=f"{shirt_text} has completed CS50P")

# save
pdf.output("shirtificate.pdf")
