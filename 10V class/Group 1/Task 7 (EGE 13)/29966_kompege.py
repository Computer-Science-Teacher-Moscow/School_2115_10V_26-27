from ipaddress import ip_network

net = ip_network('146.180.173.153/255.192.0.0', 0)

print(net[-2])
# 146191255254