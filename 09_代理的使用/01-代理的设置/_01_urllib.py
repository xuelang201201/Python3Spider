def type_basic():
    """一般代理的设置方法"""

    from urllib.error import URLError
    from urllib.request import ProxyHandler, build_opener

    proxy = '221.2.175.238:8060'

    # 如果遇到需要认证的代理，只需修改 proxy 变量，在前面加入代理认证的用户名密码即可。
    # proxy = 'username:password@221.2.175.238:8060'

    proxy_handler = ProxyHandler({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })
    opener = build_opener(proxy_handler)
    try:
        response = opener.open('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


def type_socks5():
    """SOCKS5类型的代理设置方法 需要 pip3 install PySocks"""

    import socks
    import socket
    from urllib import request
    from urllib.error import URLError

    socks.set_default_proxy(socks.SOCKS5, '117.69.244.68', 6675)
    socket.socket = socks.socksocket
    try:
        response = request.urlopen('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


if __name__ == '__main__':
    type_basic()
    # type_socks5()
