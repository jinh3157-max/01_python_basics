interfaces = [
    {"name": "Gi0/0", "status": "up", "speed": "1G"},
    {"name": "Gi0/1", "status": "down", "speed": "1G"},
    {"name": "Gi0/2", "status": "up", "speed": "10G"},
]
print(f"{'接口名称':<10}{'状态':<10}{'速度'}")
for interface in interfaces:
    print(f"{interface["name"]:<14}{interface["status"]:<12}{interface["speed"]}")