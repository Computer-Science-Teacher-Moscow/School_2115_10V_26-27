from ipaddress import ip_network

net = ip_network('111.222.0.124/255.255.224.0', 0)

for ip in net:
    ip1 = f'{ip:b}'
    if ip1.count('0') * ip1.count('1') % 2 != 0:
        print(ip)