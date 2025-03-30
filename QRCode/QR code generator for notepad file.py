import pyqrcode

# Organized text for Notepad-like display
text_data = """
WIFI:S:aliraza;T:WPA;P:ALI@84
"""
qr = pyqrcode.create(text_data)
qr.svg("notepad.svg", scale=6)

print("✅ Notepad-style QR Code generated!")
