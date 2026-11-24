from ipaddress import ip_network, ip_address

net_ip = ip_address('124.128.64.0')
for mask in range(0,33):
    net = ip_network(f'124.128.112.142/{mask}', 0)
    if net.network_address == net_ip:
        print(net.netmask)
