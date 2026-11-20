from ipaddress import ip_network

net = ip_network('192.168.32.160/255.255.255.240')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1')  % 2 == 0:
        cnt +=1
print(cnt)
print('Количество адресов в сети:', net.num_addresses)
print('Количество адресов в сети для назначения компьютеру:', net.num_addresses - 2)
print('Адрес сети:', net.network_address, net[0])
print('Широковещательный адрес сети:', net.broadcast_address, net[-1])
print('ip адрес певого компьютера:', net[1])
print('ip адрес последнего компьютера:', net[-2])
print('ip адрес предпоследнего компьютера:', net[-3])

