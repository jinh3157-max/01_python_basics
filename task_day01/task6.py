devices = [
    {"name": "CoreSwitch", "ip": "10.1.1.1", "role": "核心交换机"},
    {"name": "Firewall", "ip": "10.1.1.2", "role": "防火墙"},
    {"name": "WLC", "ip": "10.1.1.3", "role": "无线控制器"},
]
print(f"{'设备名称':<10}{'IP地址':<12}{'角色'}")
for device in devices:
    print(f"{device["name"]:<14}{device["ip"]:<14}{device["role"]}")