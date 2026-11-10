version_raw = "  Cisco IOS XE Software, Version 17.03.04  "
print("去掉空格:",version_raw.strip())
print("转大写  :",version_raw.strip().upper())
print("替换版本:",version_raw.strip().replace("17.03.04","17.06.01"))