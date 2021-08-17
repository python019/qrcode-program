import qrcode

kod = qrcode.QRCode(box_size=20, border=2)

kod.add_data("QRCode darslik.(SUSYS Python intermediate kurslari uchun)")

img = kod.make_image(fill_color="crimson", back_color="black")
img.save("qrcode.png")
