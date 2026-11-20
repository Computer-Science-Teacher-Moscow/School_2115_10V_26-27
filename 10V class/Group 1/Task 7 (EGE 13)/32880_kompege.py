from ipaddress import ip_network

net = ip_network('95.106.135.150/255.255.255.0', 0)
print('Адрес сети', net.network_address, net[0])
print('Широковещательный адрес сети', net.broadcast_address, net[-1])
print('Количество ip адресов в сети', net.num_addresses)
print('Количество компьютеров в сети', net.num_addresses - 2)
print('Адрес первого компьютера в сети', net[1])
print('Адрес последнего компьютера в сети', net[-2])

