#V-card QR code with logo in the center of it and using dots instead of squares

import qrcode
from PIL import Image, ImageDraw
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    CircleModuleDrawer, SquareModuleDrawer
)

values = ['*****', '*****', 'Software Engineer', '*****', '*****@gmail.com', 'https://t.me/*****']
vcard_data = f'BEGIN:VCARD\n' \
             f'VERSION:3.0\n' \
             f'N:{values[0]};{values[1]}\n' \
             f'TITLE:post : {values[2]}\n' \
             f'TEL;TYPE=cell:{values[3]}\n' \
             f'EMAIL:work mail : {values[4]}\n' \
             f'NOTE:Telegram - :{values[5]}\n' \
             f'END:VCARD\n'


def make_qrcode(data, border=5, image_size=(300, 300), icon_path='', factor=3.5):
    #          
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=border)
    qr.add_data(data)  # Написать данные в QR-код
    qr.make()
    # Dots instead of blocks (squares)
    qrcode_image = qr.make_image(image_factory=StyledPilImage,
                                 module_drawer=CircleModuleDrawer(resample_method=None),
                                 eye_drawer=SquareModuleDrawer(),
                               ).resize(image_size, Image.LANCZOS).convert('RGBA')

    if icon_path:  # Image in the QR center
        icon_size = int(image_size[0] / factor), int(image_size[1] / factor)
        icon = Image.open(icon_path).resize(icon_size, Image.LANCZOS).convert('RGBA')
        icon_margin = int((image_size[0] - icon_size[0]) / 2), int((image_size[1] - icon_size[1]) / 2)
        mask = Image.new('RGBA', icon_size, color='white')
        qrcode_image.paste(mask, icon_margin, mask)
        qrcode_image.paste(icon, icon_margin, icon)

    qrcode_image.save("qrcode_template.png")


if __name__ == '__main__':

    make_qrcode(data=vcard_data, icon_path='logo.png')
