import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask,HorizontalGradiantColorMask
from fpdf import FPDF
from PIL import Image

vcard_data = """BEGIN:VCARD
VERSION:3.0
S:Durai;Pandi
FN:Pandi Durai
ORG:32Mins Digital Consultancy Services
TITLE:Software Engineer
TEL:+91 9751391299
EMAIL:pandidurai32127@gmail.com
ADR:IITM-Pravartak,B5-01,B-Block,5th Floor,IIT Madras Research Park,Kanagam Road,Taramani,Chennai - 600 113
END:VCARD"""

# Generate QR Code with Circle Modules
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)
qr.add_data(vcard_data)
qr.make(fit=True)

# Customize QR code style
# img = qr.make_image(
#     image_factory=StyledPilImage,
#     module_drawer=CircleModuleDrawer(),
#     color_mask=SolidFillColorMask(
#         back_color=(255, 255, 255),
#         front_color=(12, 38, 56)  # Dark blue for the circular dots
#     )
# )

# Customize QR code style with horizontal gradient
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),
    color_mask=HorizontalGradiantColorMask(
        back_color=(255, 255, 255),
        left_color=(248, 153, 35),
        right_color=(141, 197, 67)
    )
)


# Save the circular QR code
img.save("Pandidurai_qr_circular.png")

# Generate PDF with circular QR
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="32Mins Digital Consultancy Services", ln=True, align='C')
pdf.cell(200, 10, txt="Pandi durai S - Software Engineer", ln=True, align='C')
pdf.image("Pandidurai_qr_circular.png", x=60, y=40, w=90)
pdf.output("Pandidurai_contact_dots.pdf")

print("Circular QR Code and PDF for Pandidurai created successfully!")
