import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data = input("Enter the data to encode: ")
    filename = input("Enter the filename to save the QR code (with extension, e.g., image.png): ")
    generate_qr_code(data, filename)
    print(f"QR code saved as {filename}")


