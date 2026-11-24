from ipaddress import ip_network, ip_address

net = ip_network('202.71.92.91/255.255.192.0', 0)

for ip in net:
    if net[0] < ip < net[-1] and sum(int(x) % 2 !=0 for x in str(ip).split('.')) == 2:
        print(str(ip).replace('.', ''))