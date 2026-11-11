import re
import os

route = os.popen("route -n").read()
# text = "标题\n0.0.0.0 192.168.214.2"
# result1 = re.match(r"0\.0\.0\.0", text)
# result2 = re.search(r"0\.0\.0\.0", text).group(0)
# print(result1)
# print(result2)

pattern = r"0\.0\.0\.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+UG"
result= re.search(pattern, route, re.M)
print(f"网关为: {result.group(1)}")