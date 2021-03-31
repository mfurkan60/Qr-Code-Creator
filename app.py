#import Qr code Library for Python
import pyqrcode



class CreateQrCode:
    
    
    def __init__(self,x):
        url = pyqrcode.create(x)
        url_png = url.png('png_qrCode.png',scale=6)
        url_svg = url.svg('svg_qrCode.svg', scale=6)
        print("Process completed. Please check home directory")

        
    

print("Please enter url address") 
x = input()
qrcode = CreateQrCode(x)
 
