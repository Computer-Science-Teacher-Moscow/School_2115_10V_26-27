from ipaddress import ip_network, ip_address

mask = '255.255.0.0'
res = []
for o1 in range(0,256):
    for o2 in range(0, 256):
        net = ip_network(f'{o1}.{o2}.0.0/{mask}')
        cnt = 0
        for ip in net:
            sm = sum(int(x) for x in str(ip).split('.'))
            if sm == 31: cnt +=1
        res.append((sm, net))
print(max(res)[1])
