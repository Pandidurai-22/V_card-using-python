import qrcode
from fpdf import FPDF

vcard_data = """BEGIN:VCARD
VERSION:3.0
S:Pandidurai;S
FN:Pandidurai S
ORG:IITM Research Park.
TITLE:Junior Software Engineer
TEL:+91 9751391299
EMAIL:pandidurai32127@gmail.com
END:VCARD"""


qr = qrcode.QRCode(
    version=3,  
    error_correction=qrcode.constants.ERROR_CORRECT_Q,  
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("Pandidurai.png")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Scan to Save Contact", ln=True, align='C')
pdf.image("Pandidurai.png", x=60, y=40, w=90)
pdf.output("Pandidurai.pdf")
print("QR Code and PDF created successfully!")
