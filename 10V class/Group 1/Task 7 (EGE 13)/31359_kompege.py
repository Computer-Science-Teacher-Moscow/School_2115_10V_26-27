from ipaddress import ip_network

net = ip_network('154.141.198.190/255.255.192.0', 0)

print(net[-1])
