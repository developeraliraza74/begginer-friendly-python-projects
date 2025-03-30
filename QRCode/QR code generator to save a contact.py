import pyqrcode

first_name = input("Enter your First Name : ")
contact = int(input("Enter your number : "))
email = input("Enter your mail Address : ")

contact_details = f"""BEGIN:VCARD
FN:{first_name}
TEL:{contact}
EMAIL:{email}
END:VCARD
"""

qr = pyqrcode.create(contact_details)

qr.svg(f'{first_name}Details.svg', scale=6)
print("QR code generated Successfully")
