from PIL import Image

def cle_image(image_path):
    img= Image.open(image_path)
    cle = ""
    for y in range(img.size[1]): # Parcours des bits de pixels en y
        for x in range(img.size[0]): # Parcours des bits de pixels en x
            pixel = img.getpixel((x, y))
            cle += str(pixel % 2)
            if len(cle) == 64:
                break
        if len(cle) == 64:
            break
    return cle

print(cle_image("rossignol2.bmp"))