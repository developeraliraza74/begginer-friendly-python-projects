import pyqrcode

combined_data = """Contact:
BEGIN:VCARD
VERSION:3.0
FN:Ali Raza
TEL:+923701388674
EMAIL:ar7350315@gmail.com
ADRESS:Sahiwal
END:VCARD
Wi-Fi:WIFI:S:StormFiber-5630;T:WPA2;P:JJGmJde5;;
"""

qr = pyqrcode.create(combined_data)
qr.svg("combined_qr.svg", scale=4)
print("Combined QR Code generated!")
