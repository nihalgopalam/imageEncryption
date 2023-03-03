# imageEncryption

given image takes RGB values of individual pixels. Uses RSA encryption on R, G, and B values to get a new larger value. To get new RGB values from the encrypted value, converts the values to binary and split by 8 bits to get new values for colors out of 256. Create new RGB values from the split cipher and create new image using these new pixels. 
