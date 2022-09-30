import requests
import os

"""
ip接收端：部署在终端主机。运行"ip_receiver.bat"，输入要查询地址的主机名，结果会自动被复制到剪切板。
"""

server_url = 'http://10.132.245.202:5002/'  # 更改为需要部署的服务器的url


def get_ip(desktop_name: str):
    """
    查询主机名为desktop_name的主机ip地址
    :param desktop_name: 主机名
    """

    global server_url
    if not server_url.endswith('/'):
        server_url += '/'

    ip = requests.get(server_url + 'getip?desktop_name=' + desktop_name).content.decode()
    print(ip)
    os.popen('echo ' + ip + '|clip')
    print('已将结果复制到剪切板')


if __name__ == '__main__':
    desktop_name = input('请输入要查询地址的主机名：\n')
    get_ip(desktop_name)
