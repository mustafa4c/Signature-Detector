from PIL import Image,ImageTk

img = "2.png"
### show img ###
image = Image.open(img) 

path  = "img"

### save img ###
image = image.save('{}/{}'.format(path,img))

    