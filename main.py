from PIL import Image
import random
import rsa
import math


# to create a new 10x10 image
def newImage(width, length):
    image = Image.new("RGB", (length,width))
    x = image.getdata()
    image1 = []
    for i in x:
        image1.append(((int(random.random()*256)),(int(random.random()*256)),(int(random.random()*256))))

    image.putdata(image1)
    filename = "image{width}{length}.jpg"
    image.save(filename)
    return filename


(pub, priv) = rsa.newkeys(512)


image = Image.open("image.jpg")
data = image.getdata()

original = []
cipher = []
message = []

cImage = []

for i in data:
    original.append(i[0])
    x = (str(i[0])).encode()
    encrypt = rsa.encrypt(x, pub)
    cipher.append(encrypt)
    val = str(int.from_bytes(encrypt, "big"))
    cImage.append((((1/int(val[:51]))*256), ((1/int(val[51:102]))*256), ((1/int(val[102:]))*256)))
    # print((str(1/int(val[:51])*256), str(1/int(val[51:102])*256), str(1/int(val[102:])*256)))


    

for i in cipher:
    decrypt = rsa.decrypt(i, priv)
    message.append(decrypt.decode())


print(original)
print(cImage)

image1 = Image.new("RGB", (10,10))
image1.putdata(cImage)
image1.show()

# print(string)






