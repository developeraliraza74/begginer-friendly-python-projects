import pyqrcode

ssid = input("Enter ssid : ")
password = input("Enter password : ")
security = input("Enter security type(WPA2) : ")

# Correct Wi-Fi format
wifi_data = f"WIFI:S:{ssid};T:{security};P:{password};;"


# create the qr code using pyqrcode python library
contact = pyqrcode.create(wifi_data)
contact.svg(f"{ssid} wifi qr code.svg", scale=5)

print("Contact QR code generated successfully")
