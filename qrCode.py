
import qrcode

data_to_encode = "https://vk.com/id24598723541"

qr = qrcode.QRCode(
    box_size=10,
    border=10,
)

qr.add_data(data_to_encode)

image = qr.make_image()

image.save('qrcode.png')

