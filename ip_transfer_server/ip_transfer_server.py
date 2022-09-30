import flask

"""
服务端：部署在服务器。用来保存需要被远程连接的主机发来的ip地址和为终端主机提供需要被远程连接主机的ip地址。运行”ip_transfer_server.bat“以启动服务。
"""

desktop_dict = {}
ipcheck = flask.Flask(__name__)


@ipcheck.route('/getip', methods=['GET'])
def get_ip():
    """
    根据主机名获取主机ip
    :return: 主机ip
    """
    try:
        return desktop_dict[flask.request.args['desktop_name']]
    except:
        return 'no desktop nemed "' + flask.request.args['desktop_name'] + '"'


@ipcheck.route('/offerip', methods=['GET'])
def offer_ip():
    """
    接收主机发送来的ip地址
    :return: 收到ip地址的确认信息
    """
    global desktop_dict
    desktop_dict[flask.request.args['desktop_name']] = flask.request.args['ip']
    return 'ip offered'


if __name__ == '__main__':
    ipcheck.run('0.0.0.0', 5002)
