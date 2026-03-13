# A101
# pip install qrcode[pil]

import qrcode

img = qrcode.make('https://share.google/6PvvLVLal6STFLXt5')
img.save('qrcode.png') # XD
