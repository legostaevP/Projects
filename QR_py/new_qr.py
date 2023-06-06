# import qrcode
# from PIL import Image

# website_url = 'https://pythonist.ru/\n'
# telegram_user = 'https://t.me/leg_las\n'
# email_addr = 'mailto:pvlegostaev@gmail.com\n'

# #Саша
# whats_user = 'https://wa.me/79851769085?text=Hi\n'

# # Generate QR code without logo
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10#,
#     #border=4,
# )
# # qr.add_data('https://www.example.com')
# # qr.make(fit=True)

# qr.add_data(website_url)
# qr.make(fit=True)

# qr.add_data(telegram_user)
# qr.make(fit=True)

# qr.add_data(whats_user)
# qr.make(fit=True)

# img_qr = qr.make_image(fill_color='black', back_color='white')

# # Open logo image
# logo = Image.open('TRDC.png')

# # Scale logo to 20% of QR code size
# w, h = img_qr.size
# logo_size = int(0.2 * w)
# logo = logo.resize((logo_size, logo_size))

# # Calculate position to place logo in center of QR code
# pos = ((w - logo_size) // 2, (h - logo_size) // 2)

# # Paste logo onto QR code
# img_qr.paste(logo, pos)

# # Save QR code with logo
# img_qr.save('corrected.png')
'''

import qrcode
from PIL import Image

# Define vCard data
vcard_data = 'BEGIN:VCARD\n' + \
             'VERSION:3.0\n' + \
             'N:LastName;FirstName\n' + \
             'TEL;TYPE=cell:(123) 456-7890\n' + \
             'ADR;TYPE=work:123 Main St, Anytown USA 12345\n' + \
             'EMAIL:firstname.lastname@example.com\n' + \
             'END:VCARD\n'

# Define other contact information
website_url = 'https://pythonist.ru/\n'
telegram_user = 'https://t.me/leg_las\n'
email_addr = 'mailto:pvlegostaev@gmail.com\n'
whats_user = 'https://wa.me/79851769085?text=Hi\n'

# Initialize QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10
)

# Add vCard data to QR code
qr.add_data(vcard_data)
qr.make(fit=True)

# Add other contact information to QR code
qr.add_data(website_url)
qr.make(fit=True)

qr.add_data(telegram_user)
qr.make(fit=True)

qr.add_data(whats_user)
qr.make(fit=True)

# Generate QR code image
img_qr = qr.make_image(fill_color='black', back_color='white')

# Open logo image
logo = Image.open('TRDC.png')

# Scale logo to 20% of QR code size
w, h = img_qr.size
logo_size = int(0.2 * w)
logo = logo.resize((logo_size, logo_size))

# Calculate position to place logo in center of QR code
pos = ((w - logo_size) // 2, (h - logo_size) // 2)

# Paste logo onto QR code
img_qr.paste(logo, pos)

# Save QR code with logo
img_qr.save('corrected.png')
'''

# import qrcode
# from PIL import Image

# # Define the contact information
# values = ['Doe', 'John', '(123) 456-7890', '123 Main St, Anytown USA 12345', 'john.doe@example.com']
# website_url = 'https://pythonist.ru/\n'
# telegram_user = 'https://t.me/leg_las\n'
# whats_user = 'https://wa.me/79851769085?text=Hi\n'

# # Define the vCard data using f-strings to insert values from the list
# vcard_data = f'BEGIN:VCARD\n' \
#              f'VERSION:3.0\n' \
#              f'N:{values[0]};{values[1]}\n' \
#              f'TEL;TYPE=cell:{values[2]}\n' \
#              f'ADR;TYPE=work:{values[3]}\n' \
#              f'EMAIL:{values[4]}\n' \
#              f'URL:{website_url}' \
#              f'NOTE:Telegram - {telegram_user}' \
#              f'NOTE:WhatsApp - {whats_user}' \
#              f'END:VCARD\n'

# # Generate the QR code image using the vCard data
# qr = qrcode.QRCode(version=1, box_size=10, border=5)
# qr.add_data(vcard_data)
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")

# # Add logo to the center of the QR code image
# logo = Image.open("TRDC.png")
# logo_size = 70
# img_w, img_h = img.size
# logo_w, logo_h = logo.size
# logo = logo.resize((int(logo_size * logo_w / logo_h), logo_size))
# logo_w, logo_h = logo.size
# img.paste(logo, (int((img_w - logo_w) / 2), int((img_h - logo_h) / 2)), mask=logo.convert('L'))

# # Save the resulting QR code image to a file
# img.save("qrcode.png")

#======================================================================
# import qrcode
# from PIL import Image

# # Define the contact information
# values = ['Doe', 'John', '(123) 456-7890', '123 Main St, Anytown USA 12345', 'john.doe@example.com']
# website_url = 'https://pythonist.ru/\n'
# telegram_user = 'https://t.me/leg_las\n'
# whats_user = 'https://wa.me/79851769085?text=Hi\n'

# # Define the vCard data using f-strings to insert values from the list
# vcard_data = f'BEGIN:VCARD\n' \
#              f'VERSION:3.0\n' \
#              f'N:{values[0]};{values[1]}\n' \
#              f'TEL;TYPE=cell:{values[2]}\n' \
#              f'ADR;TYPE=work:{values[3]}\n' \
#              f'EMAIL:{values[4]}\n' \
#              f'URL:{website_url}' \
#              f'NOTE:Telegram - {telegram_user}' \
#              f'NOTE:WhatsApp - {whats_user}' \
#              f'END:VCARD\n'

# # Generate the QR code image using the vCard data
# qr = qrcode.QRCode(version=5, box_size=2, border=4)
# qr.add_data(vcard_data)
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")

# # Add logo to the center of the QR code image
# logo = Image.open("TRDC.png")
# logo_size = 70
# img_w, img_h = img.size
# logo_w, logo_h = logo.size
# logo = logo.resize((int(logo_size * logo_w / logo_h), logo_size))
# logo_w, logo_h = logo.size
# img.paste(logo, (int((img_w - logo_w) / 2), int((img_h - logo_h) / 2)), mask=logo.convert('L'))

# # Save the resulting QR code image to a file
# img.save("qrcode.png")

#======================================================================


# import qrcode
# from PIL import Image

# # Define the contact information
# values = ['Doe', 'John', '(123) 456-7890', '123 Main St, Anytown USA 12345', 'john.doe@example.com']
# website_url = 'https://pythonist.ru/\n'
# telegram_user = 'https://t.me/leg_las\n'
# whats_user = 'https://wa.me/79851769085?text=Hi\n'

# # Define the vCard data using f-strings to insert values from the list
# vcard_data = f'BEGIN:VCARD\n' \
#              f'VERSION:3.0\n' \
#              f'N:{values[0]};{values[1]}\n' \
#              f'TEL;TYPE=cell:{values[2]}\n' \
#              f'ADR;TYPE=work:{values[3]}\n' \
#              f'EMAIL:{values[4]}\n' \
#              f'URL:{website_url}' \
#              f'NOTE:Telegram - {telegram_user}' \
#              f'NOTE:WhatsApp - {whats_user}' \
#              f'END:VCARD\n'

# # Generate the QR code image using the vCard data
# qr = qrcode.QRCode(version=5, box_size=2, border=4)
# qr.add_data(vcard_data)
# qr.make(fit=True)

# # Create a new image with a white border
# img = qr.make_image(fill_color="black", back_color="white")
# border_width = 10
# new_size = (img.size[0] + border_width * 2, img.size[1] + border_width * 2)
# bordered_img = Image.new('RGB', new_size, color='white')
# bordered_img.paste(img, (border_width, border_width))

# # Add logo to the center of the QR code image
# logo = Image.open("TRDC.png")
# logo_size = 70
# img_w, img_h = bordered_img.size
# logo_w, logo_h = logo.size
# logo = logo.resize((int(logo_size * logo_w / logo_h), logo_size))
# logo_w, logo_h = logo.size
# img.paste(logo, (int((img_w - logo_w) / 2), int((img_h - logo_h) / 2)), mask=logo.convert('L'))

# # Save the resulting QR code image to a file
# img.save("qrcode.png")


#======================================================================


# import qrcode
# from PIL import Image

# # Define the contact information
# values = ['Doe', 'John', '(123) 456-7890', '123 Main St, Anytown USA 12345', 'john.doe@example.com']
# website_url = 'https://pythonist.ru/\n'
# telegram_user = 'https://t.me/leg_las\n'
# whats_user = 'https://wa.me/79851769085?text=Hi\n'

# # Define the vCard data using f-strings to insert values from the list
# vcard_data = f'BEGIN:VCARD\n' \
#              f'VERSION:3.0\n' \
#              f'N:{values[0]};{values[1]}\n' \
#              f'TEL;TYPE=cell:{values[2]}\n' \
#              f'ADR;TYPE=work:{values[3]}\n' \
#              f'EMAIL:{values[4]}\n' \
#              f'URL:{website_url}' \
#              f'NOTE:Telegram - {telegram_user}' \
#              f'NOTE:WhatsApp - {whats_user}' \
#              f'END:VCARD\n'

# # Generate the QR code image using the vCard data
# qr = qrcode.QRCode(version=1, box_size=10, border=5)
# qr.add_data(vcard_data)
# qr.make(fit=True)

# # Create a new image with a white border
# img = qr.make_image(fill_color="black", back_color="white")
# border_width = 10
# new_size = (img.size[0] + border_width * 2, img.size[1] + border_width * 2)
# bordered_img = Image.new('RGB', new_size, color='white')
# bordered_img.paste(img, (border_width, border_width))

# # Add logo to the center of the QR code image
# logo = Image.open("TRDC.png")
# logo_size = 70
# img_w, img_h = bordered_img.size
# logo_w, logo_h = logo.size
# logo = logo.resize((int(logo_size * logo_w / logo_h), logo_size))
# logo_w, logo_h = logo.size
# bordered_img.paste(logo, (int((img_w - logo_w) / 2), int((img_h - logo_h) / 2)), mask=logo.convert('L'))

# # Save the resulting QR code image to a file
# bordered_img.save("qrcode.png")

#======================================================================


# import qrcode
# from PIL import Image

# # Define the contact information
# values = ['Doe', 'John', '(123) 456-7890', '123 Main St, Anytown USA 12345', 'john.doe@example.com']
# website_url = 'https://pythonist.ru/\n'
# telegram_user = 'https://t.me/leg_las\n'
# whats_user = 'https://wa.me/79851769085?text=Hi\n'

# # Define the vCard data using f-strings to insert values from the list
# vcard_data = f'BEGIN:VCARD\n' \
#              f'VERSION:3.0\n' \
#              f'N:{values[0]};{values[1]}\n' \
#              f'TEL;TYPE=cell:{values[2]}\n' \
#              f'ADR;TYPE=work:{values[3]}\n' \
#              f'EMAIL:{values[4]}\n' \
#              f'URL:{website_url}' \
#              f'NOTE:Telegram - {telegram_user}' \
#              f'NOTE:WhatsApp - {whats_user}' \
#              f'END:VCARD\n'

# # Generate the QR code image using the vCard data
# qr = qrcode.QRCode(version=1, box_size=10, border=4)
# qr.add_data(vcard_data)
# qr.make(fit=True)

# # Create a new image with a white border
# img = qr.make_image(fill_color="black", back_color="white")

# # Add logo to the center of the QR code image
# logo = Image.open("TRDC.png")
# logo_size = 70
# img_w, img_h = img.size
# logo_w, logo_h = logo.size
# logo = logo.resize((int(logo_size * logo_w / logo_h), logo_size))
# logo_w, logo_h = logo.size
# img.paste(logo, (int((img_w - logo_w) / 2), int((img_h - logo_h) / 2)), mask=logo.convert('L'))

# # Save the resulting QR code image to a file
# img.save("qrcode.png")


import qrcode
from PIL import Image
# Logo_link = 'TRDC.png'
logo = Image.open('TRDC.png')
 
# Ширина логотипа
basewidth = 200
 
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

values = ['Легостаев', 'Павел', '89163784398', '108840 Москва, Троицк, ул. Академика Франка, 16', 'legostaev@trdc.com', 'info@trdc.com']
# values = ['Doe', 'John', '(123) 456-7890', '123 Main St, Anytown USA 12345', 'john.doe@example.com', 'faewfwegfw@dwcwd.com']
website_url = 'https://trdc.com/\n'
telegram_user = 'https://t.me/leg_las\n'
whats_user = 'https://wa.me/79163784398?text=Hi\n'
# whats_user = 'https://wa.me/79851769085?text=Hi\n'

# Define the vCard data using f-strings to insert values from the list
vcard_data = f'BEGIN:VCARD\n' \
             f'VERSION:3.0\n' \
             f'N:{values[0]};{values[1]}\n' \
             f'TEL;TYPE=Телефон:{values[2]}\n' \
             f'ADR;TYPE=Адрес :{values[3]}\n' \
             f'EMAIL:Личная почта : {values[4]}\n' \
             f'EMAIL:Рабочая почта : {values[5]}\n' \
             f'URL: Сайт компании - {website_url}' \
             f'NOTE:Telegram - {telegram_user}' \
             f'NOTE:WhatsApp - {whats_user}' \
             f'END:VCARD\n'

# Generate the QR code image using the vCard data
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(vcard_data)
qr.make(fit=True)

 
# adding URL or text to QRcode
# QRcode.add_data(url)
 
# generating QR code
# QRcode.make()
 
# adding color to QR code
img = qr.make_image(fill_color="black", back_color="white")
 
# set size of QR code
pos = ((img.size[0] - logo.size[0]) // 2,
       (img.size[1] - logo.size[1]) // 2)
img.paste(logo, pos)
 
# save the QR code generated
img.save('QR.png')
 
# print('QR code generated!')