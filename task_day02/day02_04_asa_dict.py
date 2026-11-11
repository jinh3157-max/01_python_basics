import re

asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

lines = asa_conn.split("\n")

pattern = r"\w{3}\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)\s\S+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+),\s\w+\s\d{1,2}:\d{1,2}:\d{1,2},\s\w+\s(\d+),\s\w+\s(\w+)"
asa_dict = {}
for line in lines:
    result = re.match(pattern, line)
    key = ()
    value = ()
    for i in range(1,5):
        key += (result.group(i),)
    for i in range(5,7):
        value += (result.group(i),)
    
    asa_dict[key] = value

print(f"打印后的字典!\n\n{asa_dict}")

for key,value in asa_dict.items():
    print("src       : {:<16}".format(key[0]), end = " | ")
    print("src_port  : {:<6}".format(key[1]), end = " | ")
    print("dst       : {:<16}".format(key[2]), end = " | ")
    print("dst_port  : {}".format(key[3]))
    print("bytes     : {:<16}".format(value[0]), end = " | ")
    print("flags     : {}".format(value[1]))
    print("====================================================================================")