from ipaddress import ip_network, ip_address

net = ip_network('95.106.135.150/255.255.255.0', 0)
print('Адрес сети', net[0], net.network_address)
print('Широковещательный адре сети', net[-1], net.broadcast_address)
print('Количество ip адресов в сети', net.num_addresses)
print('Количество ip адресов в сети, которые могут быть назначены компьютерам', net.num_addresses - 2)
print('Адерс первого компьютера в сети', net[1])
print('Адерс последнег компьютера в сети', net[-2])


