import qrcode

img = qrcode.make("www.ganimides.ucm.cl/haraya")

f = open("output.png", "wb")
img.save(f)
f.close()