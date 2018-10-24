#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
logoIm = logoIm.resize((int(logoWidth/10), int(logoHeight/10)))
print(logoIm.size)
logoWidth, logoHeight = logoIm.size

print(logoWidth,logoHeight)

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    filename=filename.lower()
    if not (filename.endswith('.png') or filename.endswith('.jpg')or filename.endswith('.gif')or filename.endswith('.bmp')) \
       or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size
    if width<(2*logoWidth) or height<(2*logoHeight):
        continue
    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
            print(height,width)
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
            print(height,width)

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))
