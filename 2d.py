import math
from PIL import Image
from noise import perlin, noise_octaves

xy = (800, 800)

def gen_image(name, size, func, *args):
    #kx, ky, kz, kk = 0.01, 0.01, 0, 0x1000
    kx, ky, kz, kk = 0.02, 0.02, 0.0, 0x3600
    image = Image.new('I', size)
    for j in range(size[1]):
        for i in range(size[0]):
            p = func(kx*i, ky*j, kz, *args)
            image.putpixel((i, j), math.floor(p*kk))
    image.save(name)

if __name__ == '__main__':
    gen_image("no_octaves.png", xy, perlin)
    gen_image("octaves.png", xy, noise_octaves, 1, 0.5)
