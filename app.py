import pyqrcode



def createQrCode(x):
     
    url = pyqrcode.create(x)
    url_png = url.png('png_qrCode.png',scale=6)
    url_svg = url.svg('svg_qrCode.svg', scale=6)


print("Please enter url address") 
x = input()
createQrCode(x)