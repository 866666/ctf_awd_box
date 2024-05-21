# -*- coding:utf-8 -*-
# --生成ip列表--
import os

ip_header = "83.18"
ip_start = 64
ip_end = 75
port_start = 22
port_end = 23
white_list = "172.20.110.101"  # 白名单
# 删除旧文件ip_list.txt
if os.path.exists("ip_list.txt"):  # 删除旧文件
    try:
        os.remove("ip_list.txt")
    except Exception as e:
        print("Delete file fail:" + str(e))
    else:
        print("Delete file success:flag_list.txt")
with open("ip_list.txt", "w") as file:
    file.truncate(0)
for ip_x in range(ip_start, ip_end):
    for port_x in range(port_start, port_end):
        ip = ip_header + ".14" + "." + str(ip_x) + ":" + str(port_x)  # ip组合
        if ip != white_list:
            with open("ip_list.txt", "a") as file:
                file.write(ip + "\r")
            print(ip)
        else:
            print("white_list IP:" + ip)
