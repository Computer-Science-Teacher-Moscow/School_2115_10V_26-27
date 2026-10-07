# # #2
# # from math import ceil
# # size=4000*6000
# # N=2**24
# # i=24
# # V=size*i
# # print(ceil(V/2**23))
# # #3
# # size = 800 * 600
# # V = 600*2**13
# # best_i = 0
# # for i in range(1, 30):
# #     if size * i <= V:
# #         best_i = i
# #     else:
# #         break
# # print(2**best_i)
# # #4
# # size=768 * 600
# # V=420*2**13
# # for i in range(1,30):
# #     if size * i <= V:
# #         best_i = i
# #     else:
# #         break
# # print(2**best_i)
# # #6
# # size=1024*768
# # i=12
# # N=256
# # V=(size*i*N)/2**23
# # print(V)
# # #7
# # size=486*720
# # V=80*2**13
# # for i in range(1,30):
# #     if size*i*0.85<=V:
# #         best_i=i
# #     else:
# #         break
# # print(2**best_i)
# # #8
# # size=1366*1280
# # V=2000*2**13
# # for i in range(1,30):
# #     if size*i*0.75<=V:
# #         best_i=i
# #     else:
# #         break
# # print(2**best_i)
# # 9
# size = 640 * 256
# V = 170 * 2 ** 13
# for i in range(1, 30):
#     if size * i / 1.35 > V:
#         print(2 ** (i - 1))
#         break
# # #10
# # size=1280*1024
# # i=10
# # N=220
# # V=size*i*N
# # st_tr=12582912
# # t=V/st_tr
# # print(t)
# # #14?
# # '''size=1280*1024
# # N=39
# # st_tr=1966080
# # t=280
# # i=11
# # V=size*i
# # for N in range(1,1000):
# #     if (V*N)//'''
# # #ДЗ1
# # size=315*3072
# # V=735*2**13
# # for i in range(1,30):
# #     if size*i<=V:
# #         best_i=i
# #     else:
# #         break
# # print(2**best_i)
# # #ДЗ2
# # size=1280*960
# # V=320*2**13
# # for i in range(1,30):
# #     if size*i<=V:
# #         best_i=i
# #     else: break
# # print(2**best_i)
# # #ДЗ4
# # size=1920*1080
# # colors=4096
# # i=12
# # N=68
# # K=(size*i*N)/2**13
# # print(K)
# # #

