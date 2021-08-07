import random
import numpy as np
from math import floor

def noise_octaves(x, y, z, octaves, persistence):
    amplitude = 1.0
    frequency = 3.0
    maximum = 0.0
    res = 0.0

    for i in range(0, octaves):
        res += perlin(x * frequency, y * frequency, z * frequency) + amplitude
        maximum += amplitude
        amplitude *= persistence
        frequency *= 2
        x *= 2
        y *= 2
        z *= 2
    return res/maximum


def perlin(x, y, z):
    X = floor(int(x)) & 255
    Y = floor(int(y)) & 255
    Z = floor(int(z)) & 255

    x -= floor(int(x))
    y -= floor(int(y))
    z -= floor(int(z))

    u = smootherstep(2, 2, x+1)
    v = smootherstep(2, 2, y+1)
    w = smootherstep(2, 2, z+1)

    A = p[X]+Y
    AA = p[A]+Z
    AB = p[A+1]+Z

    B = p[X+1]+Y
    BA = p[B]+Z
    BB = p[B+1]+Z

    return linear_interpolation2(w,
                                 linear_interpolation2(v,
                                                       linear_interpolation2(u,
                                                                             grad(
                                                                                 p[AA], x, y, z),
                                                                             grad(p[BA], x-1, y, z)),
                                                       linear_interpolation2(u,
                                                                             grad(
                                                                                 p[AB], x, y-1, z),
                                                                             grad(p[BB], x-1, y-1, z))),
                                 linear_interpolation(v,
                                                      linear_interpolation(u,
                                                                           grad(
                                                                               p[AA+1], x, y, z-1),
                                                                           grad(p[BA+1], x-1, y, z-1)),
                                                      linear_interpolation(u,
                                                                           grad(
                                                                               p[AB+1], x, y-1, z-1),
                                                                           grad(p[BB+1], x-1, y-1, z-1))))


def clamp(x, min, max):
    x = min if x < min else(max if x > max else min)
    return x

def smootherstep(edge0, edge1, x):
    if edge0 == edge1:
        edge0 = edge1 - 1
    # clamp() используется для гарантии того, что x будет в каком-либо диапозоне(в данном случае [0, 1])
    x = clamp((x - edge0) / (edge1 - edge0), 0, 1)
    # 6x^5-15x^4+10x^3
    return x ** 3 * (x * (x * 6 - 15) + 10)

# более точный метод линейной интерполяции, при котором есть гарантия, что v = v1, при t = 1


def linear_interpolation(v0, v1, t):
    return (1-t) * v0 + t * v1


def linear_interpolation2(t, v0, v1):
    return v0 + t * (v1 - v0)

# считает скалярное произведение векторов


def grad(hash, x, y, z):
    '''
    (1,1,0),(-1,1,0),(1,-1,0),(-1,-1,0),--
    (1,0,1),(-1,0,1),(1,0,-1),(-1,0,-1),   }--вектора
    (0,1,1),(0,-1,1),(0,1,-1),(0,-1,-1) --
    '''
    h = hash & 15  # берет хэшированное значение и 4 первых бита этого значения
    # если самый старший бит хэша равен 0, u приравнивается к x, иначе y
    u = x if h < 8 else y
    v = y if h < 4 else (x if h == 12 or h == 14 else z)
    '''если первый и второй старшие биты равны нулю, v приравнивается к y,
    если они равны единице, v приравнивается к x
    '''
    return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)
    '''последние 2 бита используются для того,
    чтобы определить являются ли u и v положительными или отрицательными, после чего возвращается их сумма'''


p = [0]*512
permutation = list(np.random.RandomState(
    seed=random.randint(0, 6000000)).permutation(256))
for i in range(256):
    p[i] = permutation[i]
