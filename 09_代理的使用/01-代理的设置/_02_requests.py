def type_basic():
    """一般代理的设置方法"""

    import requests
    proxy = '180.124.87.176:4216'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


def type_socks5():
    """SOCKS5类型的代理设置方法 需要 pip3 install 'requests[socks]' """

    import requests
    proxy = '183.166.253.239:6666'
    proxies = {
        'http': 'socks5://' + proxy,
        'https': 'socks5://' + proxy,
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


def type_socks5_2():
    """第 2 种设置方法"""
    import requests
    import socks
    import socket

    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9742)
    socket.socket = socks.socksocket
    try:
        response = requests.get('http://httpbin.org/get')
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


if __name__ == '__main__':
    type_basic()
    # type_socks5()
    # type_socks5_2()
