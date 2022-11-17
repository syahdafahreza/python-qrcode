import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://wa.me/6285100581168')
qr.make(fit=True)

img = qr.make_image(fill_color=(221, 19, 123), back_color="white")
img.save("scan-me.png")