import requests
import os
import re
import time

"""
ip发送端：部署在需要被远程访问的主机上。运行“refresh_ip_offerer.bat”将该源码打包为“ip_offerer.exe”，并手动将ip_offerer.exe设为开机启动项。其将会间隔一段时间向服务器发送本机ip地址。
"""


def offer_ip(server_url: str, desktop_name: str, sleep_time: int):
    """
    向服务器以sleep_time为间隔发送本机ip
    :param server_url:服务器url
    :param desktop_name:主机名
    :param sleep_time:间隔时间
    """

    if not server_url.endswith('/'):
        server_url += '/'

    # 获取本机ip
    ipconfig = os.popen('ipconfig').read()
    ipconfig = ipconfig.replace('\n', '')
    ip = re.search('无线局域网适配器 WLAN:.+子网掩码', ipconfig).group()
    ip = re.search('IPv4 地址 . . . . . . . . . . . . : .+   子网掩码', ip).group()
    ip = re.search(r'((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))',
                   ip).group()

    # 间隔一定时间向服务器发送本机ip
    while True:
        try:
            con1 = requests.get(server_url + 'offerip?ip=' + ip + '&desktop_name=' + desktop_name).content.decode()
            print(con1)
            time.sleep(sleep_time)
        except:
            pass


if __name__ == '__main__':
    server_url = 'http://10.145.78.160:5002/'  # 更改为需要部署的服务器的url
    desktop_name = 'Y7000P'  # 更改为本机名称（自定义）
    sleep_time = 600  # 发送间隔
    offer_ip(server_url, desktop_name, sleep_time)
