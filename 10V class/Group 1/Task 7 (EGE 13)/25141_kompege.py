from ipaddress import ip_network

net = ip_network('46.29.170.214/255.255.128.0', 0)

for ip in net:
    ip1 = sorted(map(int, str(ip).split('.')))
    if ip1[-1] == sum(ip1[:-1]):
        print(ip)
# 4629255180