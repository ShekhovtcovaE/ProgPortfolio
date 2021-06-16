import pyqrcode
import png
import random

def random_number():
   return random.randint(0, 255)

s = input('Type smth... ')
 
qr = pyqrcode.create(s)
qr.svg("myqr.svg", scale = 8)

print(random_number())
qr.png('file.png', scale = 8, module_color=(random_number(), random_number(), random_number(), random_number()))
