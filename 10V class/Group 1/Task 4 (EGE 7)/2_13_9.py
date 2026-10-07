size = 7680 * 4320
i = 16
v_to_flash = 9 * 2 ** 33
N = 4010
v_photo = size * i
n_photos_to_one_flash = v_to_flash // v_photo
print(n_photos_to_one_flash)
n_last_flash = N % n_photos_to_one_flash
print(n_last_flash)