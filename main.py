from PIL import Image
import random
import rsa
import math
import os

# generate a new base image to encrypt
def imageGeneration(width, length):
    image = Image.new("RGB", (length,width))
    x = image.getdata()
    image1 = []
    # get random rgb values for each pixel
    for i in x:
        image1.append((random.randint(0,256)),(random.randint(0,256)),(random.randint(0,256)))
    image.putdata(image1)
    filename = "image.jpg"
    image.save(filename)
    return filename

# generate public and private rsa keys and save to file
def keyGeneration():    
    publicKeyFile = open('publicKeyRSA', 'w+b')
    privateKeyFile = open('privateKeyRSA', 'w+b')
    (pub, priv) = rsa.newkeys(512)
    publicKeyFile.write(pub.save_pkcs1())
    privateKeyFile.write(priv.save_pkcs1())
    return publicKeyFile, privateKeyFile

# get the keys from files
public = open('publicKeyRSA', 'rb')
private = open('privateKeyRSA', 'rb')
publicKey = rsa.PublicKey.load_pkcs1(public.read())
privateKey = rsa.PrivateKey.load_pkcs1(private.read())

image = Image.open("image.jpg")
data = image.getdata()

original = []
cipher = []
message = []
cipherImage = []

# todo: fix trucatating values when spliting
for i in data:
    original.append(i[0])
    x = (str(i[0])).encode()
    encrypt = rsa.encrypt(x, publicKey)
    cipher.append(encrypt)
    val = str(int.from_bytes(encrypt, "big"))
    cipherImage.append((((1/int(val[:51]))*256), ((1/int(val[51:102]))*256), ((1/int(val[102:]))*256)))
    # print((str(1/int(val[:51])*256), str(1/int(val[51:102])*256), str(1/int(val[102:])*256)))


    

for i in cipher:
    decrypt = rsa.decrypt(i, privateKey)
    message.append(decrypt.decode())


print(original)
print(cipherImage)

image1 = Image.new("RGB", (10,10))
image1.putdata(cipherImage)
image1.show()

# print(string)












