size = 7680 * 4320
i = 16
v_foto = size * i
N = 4010
v_flash = 9 * 2 ** 33
n_to_flash = v_flash // v_foto
print(N % n_to_flash)
