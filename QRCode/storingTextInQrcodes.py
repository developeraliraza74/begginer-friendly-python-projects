import pyqrcode

data = """
Contact Details : 
Name = "Ali Raza"
Roll # : 09
Class : BSCS A 2024 
Fav. Teacher = Dr. Ammar Ashraf

Wifi Details :

SSID : Riphah Sahiwal 
Password : dummy123
Security : WPA


Save this and connect manually 
"""

qr = pyqrcode.create(data)
qr.svg("textData.svg", scale=7)
print("QR Generated Successfully")
