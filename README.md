# ip_delivery
查询远程主机ip地址

程序包含三部分：
- ip_offerer：ip提供端：部署在需要被远程访问的主机上。运行“refresh_ip_offerer.bat”将该源码打包为“ip_offerer.exe”，并手动将ip_offerer.exe设为开机启动项。其将会间隔一段时间向服务器发送本机ip地址。
- ip_transfer_server：服务端：部署在服务器。用来保存需要被远程连接的主机发来的ip地址和为终端主机提供需要被远程连接主机的ip地址。运行”ip_transfer_server.bat“以启动服务。
- ip_receiver：ip接收端：部署在终端主机。运行"ip_receiver.bat"，输入要查询地址的主机名，结果会自动被复制到剪切板。

