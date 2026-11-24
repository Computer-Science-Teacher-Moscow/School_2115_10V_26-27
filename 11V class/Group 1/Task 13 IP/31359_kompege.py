from ipaddress import ip_network, ip_address

net = ip_network('154.141.198.190/255.255.192.0', 0)
print(net[-1])
print(sum(int(x) for x in str(net[-1]).split('.')))



