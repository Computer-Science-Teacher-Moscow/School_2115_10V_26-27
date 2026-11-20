from ipaddress import ip_network

net = ip_network('192.168.12.207/255.192.0.0', 0)

for ip in net:
    ip1 = f'{ip:b}'
    if ip1.count('1') == 16:
        pass
        # print(ip)
print(net[-1])
# 1921912540

