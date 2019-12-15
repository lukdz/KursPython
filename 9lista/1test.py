import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

def gen_key(length):
    return np.random.randint(256, size=length)

def xor(a, b):
    print('xor', a, b) 
    return np.bitwise_xor(a, b)

def encode(text, key):
    text_int = [ord(c) for c in text]
    text_enc = np.bitwise_xor(text_int, key)
    text_bin = ''.join(np.binary_repr(i, width=8) for i in text_enc)
    return text_bin

def decode(text, key):
    w = 8
    text_arr = [text[i:i + w] for i in range(0, len(text), w)]
    text_enc = [int(i, 2) for i in text_arr]
    key_arr = [key[i:i + w] for i in range(0, len(key), w)]
    key_enc = [int(i, 2) for i in key_arr]
    text_dec = xor(text_enc, key_enc)
    text_str = ''.join(chr(i) for i in text_dec)
    return text_str

def picture_write(img, text):
    p = 0
    for i in range(img.shape[0]):  
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if p == len(text):
                    return                
                img[i, j, k] = np.bitwise_xor(img[i, j, k], int(text[p]))
                p = p+1

def picture_read(img, length):
    p = 0
    text = ''
    for i in range(img.shape[0]):  
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if p == length:
                    return text            
                text = text + str(np.bitwise_and(img[i, j, k], 1))
                p = p+1
        
text = 'Ala ma kota'
print( 'text', text )

key = gen_key( len(text) )
print( 'key', key )

text_enc = encode(text, key)
print( 'text_enc', text_enc)

img = []
img.append(mpimg.imread('./ii1.jpg'))
img.append(mpimg.imread('./ii2.jpg'))
img.append(img[0].copy()) 
img.append(img[1].copy())

picture_write(img[2], text_enc)
picture_write(img[3], key)
text_read = picture_read(img[2], len(text_enc))
key_read = picture_read(img[3], len(text_enc))

# print( type(text_enc), type(key) )
# print( text_enc, key )
# print( type(text_read), type(key_read) )
# print( text_read, key_read )
text_dec = decode(text_read, key_read)
print( 'text_dec', text_dec )

f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(img[0])
axarr[0,1].imshow(img[1])
axarr[1,0].imshow(img[2])
axarr[1,1].imshow(img[3])
plt.show()

# print( mpimg.imread('./ii1.jpg'))
