from ipaddress import ip_network

net = ip_network('172.16.160.0/255.255.240.0')

cnt = 0
for ip in net:
    ip = f'{ip:b}'
    if ip.count('1') % 2 == 0:
        cnt += 1
print(cnt)