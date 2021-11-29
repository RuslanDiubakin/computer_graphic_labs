from PIL import Image

def createImage(fileName, imageName, size = (540, 960)):
    img = Image.new("RGB", size, "white")
    f = open(fileName, "r")
    data = f.read().split("\n")

    for i in range(len(data) - 1):
        data[i] = data[i].split(" ")
        img.putpixel((int(data[i][0]), int(data[i][1])), (0, 0, 0))
    
    img.save(f"{imageName}.png")


createImage("DS4.txt", "image1")

