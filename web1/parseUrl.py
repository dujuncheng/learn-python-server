import socket
import ssl
# 一段可以解析URL的函数，可以解析出protocol,host, path, port
def parse_url(url):
    protocol = 'http'
    # 首先确定 protocol
    if (url[:7] == 'http://'):
        protocol = 'http'
        u = url.split('://')[1]
    elif (url[:8] == 'https://'):
        protocol = 'https'
        u = url.split('://')[1]
    else:
        u = url

    # 确定 host和path
    i = u.find('/')
    if (i == -1):
        host = u
        path = '/'
    else:
        host = u[:i]
        path = u[i:]


    # 确定port
    port_dict = {
        'http': '80',
        'https': '443'
    }
    if (host.find(':') > 0):
        port =  host.split(':')[1]
        host = host.split(':')[0]
    else:
        port = port_dict[protocol]


    return protocol, host, port, path


# 单元测试
def test_parse_url():
    test_items = [
        ('http://baidu.com',('http','baidu.com','80','/')),
        ('https://goggle.com',('https','goggle.com','443','/')),
        ('goggle.com:88/test',('http','goggle.com','88','/test')),
        ('https://sadfadasdf:88/testsadfa',('https','sadfadasdf','88','/testsadfa')),
    ]
    #
    # for x in [] 用于遍历数组，和js不同，js里面forin用于遍历对象
    for t in test_items:
        #  类似于es6 的结构赋值
        url, right_result = t
        get_result = parse_url(url)
        result_str = "parse_url err, ({}) expect({}),get ({})".format(url,right_result,get_result)
        # 使用 arrsert 断言，最后一个是如果错误的时候，应该报错的
        assert  get_result == right_result,result_str



# 根据协议头来建立连接
# http的协议是 socket.socket()连接方式
# https的协议是 ssl.wrap_socket(socket.socket())连接方式
# 最后返回 socket的实例
def socket_by_protocol(protocol):
    if (protocol.find('https"//') > -1):
        s =  socket.socket()
    elif (protocol == 'http'):
        s = ssl.wrap_socket(socket.socket())
    return s


#  模拟浏览器发出请求
def get (url):
    protocol, host, port, path= parse_url(url)

    s = socket_by_protocol(protocol)
    s.connect((host, port))

    req = 'GET {} HTTP/1.1\r\nhost: {}\r\nConnection: close\r\n\r\n'.format(path, host)
    s.send(req.encode('utf-8'))



