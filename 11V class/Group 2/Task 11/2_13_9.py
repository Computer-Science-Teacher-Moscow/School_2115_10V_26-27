size = 7680 * 4320
i = 16
v_flash = 9 * 2 ** 33
N = 4010
v_foto = size * i
n_foto_on_1_flash = v_flash // v_foto
n_last_flash = N % n_foto_on_1_flash
print(n_last_flash)
