import re
mac_table = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'

pattern = r"(\d+)\s+([\da-fA-F.]+)\s+(\w+)\s+(\w+\d/\d/\d+)"

result = re.match(pattern, mac_table)


print("{:<6}: {}".format("VLAN", result.group(1)))
print("{:<6}: {}".format("MAC", result.group(2)))
print("{:<6}: {}".format("TYPE", result.group(3)))
print("{:<6}: {}".format("PORT", result.group(4)))