from math import ceil, log2

k = 256
i = ceil(log2(k))
size = 1280 * 1024
v_flash = 4 * 2 ** 33
N_photos = 8_921_742_524
v_photo = i * size
n_photos_to_flash = v_flash // v_photo
n_last_flash =N_photos % n_photos_to_flash
print(n_last_flash)

