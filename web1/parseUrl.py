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
        s =  ssl.wrap_socket(socket.socket())
    elif (protocol == 'http'):
        s = socket.socket()
    return s


#  模拟浏览器发出请求
def get (url):
    protocol, host, port, path= parse_url(url)

    s = socket_by_protocol(protocol)
    s.connect((host, int(port)))


    req = 'GET {} HTTP/1.1\r\nhost: {}\r\nConnection: close\r\n\r\n'.format(path, host)
    s.send(req.encode('utf-8'))

    response = response_by_socket(s)
    r = response.decode('utf-8')

    status_code, headers, body =parsed_response(r)
    if status_code in ['301','302']:
        url = headers['Location']

        return get(url)

    return status_code, headers, body


def response_by_socket(s):
    res = b''
    buffer_size = 2014
    while True:
        r = s.recv(buffer_size)
        if (len(r) > 0):
            res  = res + r
        elif (len(r) == 0):
            break

    return res





def parsed_response(r):
    header, body = r.split('\r\n\r\n', 1)
    header_list = header.split('\r\n')
    status_code =  header_list[0].split(  )[1]
    rest = header_list[1:]
    headers = {}

    for item in rest:
        key = item.split(':',1)[0]
        value = item.split(':',1)[1]
        headers[key] = value

    return  status_code, headers, body



get('www.baidu.com/sss')
