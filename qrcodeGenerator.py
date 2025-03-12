import qrcode

data = input("Enter Text or URL : ").strip()
filename = input("Enter file name : ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print("QR code generated successfully")
