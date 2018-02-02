import socket


# 服务器的 host 为空字符串, 表示接受任意 ip 地址的连接
# post 是端口, 这里设置为 2000, 随便选的一个数字
host = ''
port = 2000

# s 是一个 socket 实例
s = socket.socket()
# s.bind 用于绑定
# 注意 bind 函数的参数是一个 tuple
s.bind((host, port))


# 用一个无限循环来处理请求
while True:
    s.listen(5)

    connection, address = s.accept()

    request = connection.recv(1024)

    print('ip and request, {}\n{}'.format(address, request.decode('utf-8')))

    response = b'<h1>Hello World!</h1>'

    connection.sendall(response)
    connection.close()
