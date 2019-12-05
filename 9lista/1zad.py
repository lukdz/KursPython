import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

def gen_key(length):
    key = np.random.randint(256, size=length)
    return ''.join(np.binary_repr(i, width=8) for i in key)

def xor(a, b):
    # print('xor a    ', a) 
    # print('xor b    ', b) 
    w = 8
    text_arr = [a[i:i + w] for i in range(0, len(a), w)]
    text_enc = [int(i, 2) for i in text_arr]
    key_arr = [b[i:i + w] for i in range(0, len(b), w)]
    key_enc = [int(i, 2) for i in key_arr]
    return np.bitwise_xor(text_enc, key_enc)

def encode(text, key):
    text_int = [ord(c) for c in text]
    text_bin = ''.join(np.binary_repr(i, width=8) for i in text_int)
    text_enc = xor(text_bin, key)
    text_bin = ''.join(np.binary_repr(i, width=8) for i in text_enc)
    return text_bin

def decode(text, key):
    text_dec = xor(text, key)
    text_str = ''.join(chr(i) for i in text_dec)
    return text_str

def picture_write(img, text):
    length = np.binary_repr(len(text), width=8)
    for j in range(8):
        img[0, j, 0] = np.bitwise_and(int(length[j]),np.bitwise_or(img[0, j, 0], 1))
    # print('write', len(text))

    p = 0
    for i in range(1, img.shape[0]):  
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if p == len(text):
                    return                
                img[i, j, k] = np.bitwise_and(int(text[p]),np.bitwise_or(img[i, j, k], 1))
                p = p+1

def picture_read(img):
    length_str = ''
    for j in range(8):
        length_str += str(np.bitwise_and(img[0, j, 0], 1))
    length = int(length_str,2)

    p = 0
    text = ''
    for i in range(1, img.shape[0]):  
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if p == length:
                    return text            
                text = text + str(np.bitwise_and(img[i, j, k], 1))
                p = p+1
        
text = 'Ala ma kota'
print( 'text', text )

key = gen_key( len(text) )
print( 'key      ', key )

text_enc = encode(text, key)
print( 'text_enc ', text_enc)

img = []
img.append(mpimg.imread('./ii1.jpg'))
img.append(mpimg.imread('./ii2.jpg'))
img.append(img[0].copy()) 
img.append(img[1].copy())

picture_write(img[2], text_enc)
picture_write(img[3], key)
text_read = picture_read(img[2])
key_read = picture_read(img[3])

print( 'text_read', text_read )
print( 'key_read ', key_read )
text_dec = decode(text_read, key_read)
print( 'text_dec ', text_dec )

f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(img[0])
axarr[0,1].imshow(img[1])
axarr[1,0].imshow(img[2])
axarr[1,1].imshow(img[3])
plt.show()
