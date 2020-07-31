# per_noise_3d
Ken Perlin's noise procedural generation with multi-octaves algorithm realization.
Суть алгоритма:
построение сетки, выборка случайных градиентных векторов для каждого квадрата в сетке, далее для каждого пикселя найти вектора к нему от углов квадрата, посчитать скалярное произведение между градиентами и векторами к точке, проинтерполировать одно до другого, потом так же проинтерполировать проинтерполированные значения между собой, где сетка - это просто деление картинки на квадраты, скалярное произведение векторов расстояния и градиента считается по формуле: A * B = A.x*B.x + A.y*B.y + A.z*B.z(для трехмерного пространства)


![alt text](https://github.com/Refffy/per_noise_3d/blob/master/octaves.png?raw=true)
![alt text](https://github.com/Refffy/per_noise_3d/blob/master/no_octaves.png?raw=true)
