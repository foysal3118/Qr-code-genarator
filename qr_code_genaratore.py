import segno
text = input()
qrcode = segno.make_qr(text)
path = r"D:\MY CODES\Python\reallife python\qr code images" #This path needs to be at your preference
a = '\\'
qrcode.save(f'{path}{a}qr.png',scale = 10) #You can set your picture size in scale