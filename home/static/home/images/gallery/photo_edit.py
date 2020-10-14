from PIL import Image
for i in range(18):
    fil = str(i)+"_new1.jpg"
    im = Image.open(fil)
    # width, height = im.size
    # new_height = height*800//width
    newsize = (0,0,800, 560)
    # newsize=(800,new_height)
    im1 = im.crop(newsize)
    fil = str(i)+"_new1.jpg"
    im1.save(fil)