import qrcode

n = int(input("How many QR codes would you like to generate? "))

for i in range(1, n + 1):
    print(f"\nQR Code #{i}")
    data = input("Enter the text or URL: ").strip()
    fill = input("Enter the QR code color (e.g., black, blue): ").strip()
    bg = input("Enter the background color (e.g., white, yellow): ").strip()
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=bg)
    filename = f"qr_code_{i}.png"
    img.save(filename)
    print(f" QR code saved as: {filename}")
