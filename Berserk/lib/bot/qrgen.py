import pyqrcode
import png
from pyqrcode import QRCode

# Saving your QR Code in .png format
def saveQrPng(uid):
    url = pyqrcode.create(uid)
    url.png(r'D:\GitHub\Berserk\Berserk\qrcodeenc\{0}.png'.format(uid), scale=10)

# Saving your QR Code in .svg format
def saveQrSvg(uid):
    url = pyqrcode.create(uid)
    url.svg("{0}.svg".format(uid), scale=8)