
# 一段可以解析URL的函数，可以解析出protocol,host, path, port
def parseUrl(url):
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
        'http': 80,
        'https': 443
    }
    if (host.find(':') > 0):
        port =  host.split(':')[1]
        host = host.split(':')[0]
    else:
        port = port_dict[protocol]


    return protocol, host, port, path


print(parseUrl('https://baidu.com:8888/test123'))

