import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
               error_correction=qrcode.constants.ERROR_CORRECT_L,
               box_size=10,border=4,)
data="https://www.instagram.com/"
qr.add_data(data)
img=qr.make_image(fill_color="black",back_color="white")
img.save("instagram_qr.png")