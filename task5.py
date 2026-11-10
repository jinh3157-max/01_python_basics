import random
ip = []
for i in range(4):
    ip.append(str(random.randint(1, 255)))
print("随即生产的的IPv4地址为:",'.'.join(ip))