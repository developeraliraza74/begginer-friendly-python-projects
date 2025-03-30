import pyqrcode
from pyqrcode import QRCode


link = input("Input your link : ")
url = pyqrcode.create(link)

url.svg("image.svg", scale=4)

