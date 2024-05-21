import socket
import paramiko
from concurrent.futures import ThreadPoolExecutor

# 用户名和密码列表
ssh_credentials = [("root", "123456"), ("kali", "kali"), ("kali", "shangjin")]

# IP和端口列表，假设每行是一个IP:Port
with open("host_list.txt", "r") as file:
    host_ports = file.read().splitlines()

# 使用线程池
with ThreadPoolExecutor(max_workers=5) as executor:  # 可以根据需要调整线程数量
    for host_port in host_ports:
        ip, port = host_port.split(":")

        # 检查端口是否开放
        def check_and_connect(ip, port, ssh_credentials):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)  # 设置超时时间
            if sock.connect_ex((ip, int(port))) == 0:
                print(f"端口 {port} 在 {ip} 上开放，尝试连接...")
                for user, password in ssh_credentials:
                    try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(
                            ip, port=int(port), username=user, password=password
                        )

                        # 执行命令并获取结果
                        stdin, stdout, stderr = ssh.exec_command("uname -a")
                        result = stdout.read().decode()
                        print(
                            f"用户 {user} :密码 {password} 登录 {ip} 成功，命令执行的结果：\n{result}"
                        )

                        ssh.close()
                        return  # 成功连接后退出函数
                    except (
                        paramiko.AuthenticationException,
                        paramiko.SSHException,
                    ) as e:
                        print(f"连接失败，错误信息：{e}")

                sock.close()

        # 将任务提交到线程池
        executor.submit(check_and_connect, ip, port, ssh_credentials)
