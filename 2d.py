import math
import numpy as np
from PIL import Image
from noise import perlin, noise_octaves

xy = (265, 265) #установка размера
blue = (65,105,225) #цвета
green = (34,139,34)
beach = (238, 214, 175)
snow = (255, 250, 250)
mountain = (139, 137, 137)

def gen_image(name, size, func, *args):
    kx, ky, kz, kk = 0.02, 0.02, 0.0, 0x3600
    image = Image.new('I', size)
    for j in range(size[1]):
        for i in range(size[0]):
            p = func(kx*i, ky*j, kz, *args)
            image.putpixel((i, j), math.floor(p*kk))
    image.save(name)

def generate_terrain(name, func, *args):
    kx, ky, kz = 0.01, 0.02, 4
    image = Image.new('P', xy)
    world = np.zeros(xy)
    for i in range(xy[0]):
        for j in range(xy[1]):
            world[i][j] = func(kx*i, ky*j, kz, *args)
            if world[i][j] > 0.55:
                image.putpixel((i, j), blue)
            if world[i][j] > 1.0:
                image.putpixel((i, j), beach)
            if world[i][j] > 1.1:
                image.putpixel((i, j), green)
            if world[i][j] > 1.4:
                image.putpixel((i, j), mountain)
            if world[i][j] > 1.6:
                image.putpixel((i, j), snow)
    image.save(name)

if __name__ == '__main__':
    #gen_image("no_octaves.png", xy, perlin)
    #gen_image("octaves.png", xy, noise_octaves, 1, 0.5) визуальная работа алгоритма в черно-белом цвете
    generate_terrain("terrain.png", noise_octaves, 2, 0.5) #больше двух октав лучше не устанавливать, т.к кучность и четкость картинки теряется
    print('''
         ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗███████╗██████╗ ██╗
        ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██║
        ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   █████╗  ██║  ██║██║
        ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██╔══╝  ██║  ██║╚═╝
        ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ███████╗██████╔╝██╗
         ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═════╝ ╚═╝
    ''')
