import requests

ip_a = "http://83.18.14."
for i in range(60, 254):
    ip = ip_a + str(i) + "/.shell.php"
    try:
        re = requests.get(ip, timeout=0.1)
        print(ip)
        if re.status_code == 200:
            print({ip})
        else:
            pass
    except Exception as e:
        # print(f"{ip}:error")
        pass
