import qrcode

# URL for the QR code (replace with your GitHub homepage link)
url = "https://github.com/Deva-24"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code and save it
img = qr.make_image(fill="black", back_color="white")
img.save("github_qr.png")
