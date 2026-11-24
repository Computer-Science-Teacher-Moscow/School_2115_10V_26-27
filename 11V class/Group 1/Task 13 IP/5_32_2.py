from ipaddress import ip_network, ip_address

net_ip = ip_address('111.81.192.0')
ip_host = ip_address('111.81.208.27')
for mask in range(0,33):
    net = ip_network(f'{ip_host}/{mask}', 0)
    if net.network_address == net_ip and net[0] < ip_host<net[-1]:
        print(net.netmask)
