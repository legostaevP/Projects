import qrcode
from PIL import Image
from custom_image import CustomImage

version = 4
border = 1
box_size = 30
qr = qrcode.QRCode(
    version=version,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=box_size,
    border=border,
    image_factory=CustomImage,
)

qr.add_data('Some dta')
qr.make(fit=True)


img = qr.make_image(fill_color="white", back_color="white", body="point", version=version,
                    eye_ball="ball0", eye="eye0")
img.save('qrcode.png')

im = Image.open('qrcode.png')
# im = im.convert('RGBA')
logo = Image.open('TRDC.png')
logo_scale = version/1.5 if version > 4 else version/1.25
pixel_size = (17 + version * 4 + 2 * border) * box_size
box = (int(pixel_size/2-(100*logo_scale)), int(pixel_size/2-(25*logo_scale)),
       int(pixel_size/2+(100*logo_scale)), int(pixel_size/2+(25*logo_scale)))

im.crop(box)
region = logo
region = region.resize((box[2]-box[0], box[3]-box[1]))
im.paste(region, box)
im.show("qrcodex.png")
im.save("qrcodex.png")