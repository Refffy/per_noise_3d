import datetime
from math import floor
 
def noise_octaves(x, y, z, octaves, persistence):
    amplitude = 1.0
    frequency = 1.0
    maximum = 0.0
    res = 0.0

    for i in range(0, octaves):
        #res += perlin(x + frequency, y + frequency, z + frequency) * amplitude 
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

    return linear_interpolation2(w, linear_interpolation2(v, linear_interpolation2(u, grad(p[AA], x, y, z), grad(p[BA], x-1, y, z)), 
           linear_interpolation2(u, grad(p[AB], x, y-1, z), grad(p[BB], x-1, y-1, z))),
           linear_interpolation(v, linear_interpolation(u, grad(p[AA+1], x, y, z-1 ), grad(p[BA+1], x-1, y, z-1)),
           linear_interpolation2(u, grad(p[AB+1], x, y-1, z-1), grad(p[BB+1], x-1, y-1, z-1 ))))

def clamp(x, minimal, maximal):
    if x < minimal:
        x = minimal
    elif x > maximal:
        x = maximal
    return x

def smootherstep(edge0, edge1, x):
    if edge0 == edge1:
        edge0 = edge1 - 1
    #clamp() используется для гарантии того, что x будет в каком-либо диапозоне(в данном случае [0, 1])
    x = clamp((x - edge0) / (edge1 - edge0), 0, 1)
     #6x^5-15x^4+10x^3
    return x ** 3 * (x * (x * 6 - 15) + 10)

#более точный метод линейной интерполяции, при котором есть гарантия, что v = v1, при t = 1
def linear_interpolation(v0, v1, t):
    return (1-t) * v0 + t * v1

def linear_interpolation2(t, v0, v1):
    return v0 + t * (v1 - v0)

def grad(hash, x, y, z):
    h = hash & 15
    u = x if h < 8 else y
    v = y if h < 4 else (x if h == 12 or h == 14 else z)
    return (u if (h&1) == 0 else -u) + (v if (h&2) == 0 else -v)

p = [0]*512
#np.random.RandomState(seed=0).permutation(256)
permutation = [158,  83, 170, 101, 150, 200, 118, 236,  63, 135, 149, 235, 109,
       189, 153,  73, 207, 171, 157,  97, 188,  45, 245, 138, 110, 255,
         8,  55, 222,  37, 196, 126, 111, 198, 168, 145, 187,   5,  22,
       191, 125,  12, 186, 179,  90, 129, 223,  44,  64, 182,  71, 162,
       159,  76,  59, 215, 232,  18, 224,  15, 152,  74,   7,  89, 184,
       249,  33, 108, 156, 229, 246, 214,  92,  16,  96,  75, 107, 176,
         4, 116,  61, 124,  52,  66,  26, 234, 154, 227,  40,  13,   3,
       106,  24,  30, 228,  60,  56, 139, 122,  19, 190, 136,  54, 204,
        80,  51,   2, 220, 104, 134,  86,  10, 144, 181, 238,  41,  14,
        27,  50, 231,  20, 180,  46, 173, 251, 123, 212, 178,  62, 210,
       166, 130, 155, 137,  43, 199, 146, 161, 112, 206,  98, 160,  93,
       201, 244, 113,   0,  94,  95,  69,  49,  48,  85, 253, 141,  23,
       225, 143,  78, 100, 131, 205, 254,   6,  68,  84, 121, 239, 219,
       217, 247, 194,  91, 218, 233,  11, 119, 102,  35,  57, 169,  65,
         1, 120, 203,  42, 105, 132, 221,  17,  38, 133,  53, 164, 250,
       128,  34,  28, 183, 114, 163, 151, 202,  31, 209, 127, 185, 226,
       237,  32, 167, 142, 213, 147,  29, 177, 241,  99,  82, 252, 175,
        79, 197, 208, 115, 148, 248,  72,  77,  25, 165,  81, 240, 174,
       243,  39, 230, 193,  58, 140,  88, 216,  70,  87,  36, 242,  21,
       211,   9, 103, 195,  67, 192, 117,  47, 172]

for i in range(256):
    p[256+i] = p[i] = permutation[i]

if __name__ == '__main__':
    print(perlin(3.14, 42, 7), "-просто шум")
    print("------------------")
    print(noise_octaves(3.14, 42, 7, 5, 0.5), "-шум с октавами")
    print("------------------")
    begin = datetime.datetime.now()
    print(datetime.datetime.now() - begin)
