from ipaddress import ip_network, ip_address

net = ip_network('192.168.159.86/255.255.252.0', 0)
print(net[0])
print(sum(int(x) for x in str(net[0]).split('.')))



