from ipaddress import ip_network

net = ip_network('192.168.159.86/255.255.252.0', 0)
print(net[0])