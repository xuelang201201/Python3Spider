import requests
import logging

from requests.packages import urllib3


def sslerror():
    """证书验证错误"""
    response = requests.get('https://www.zimuku.la/')
    print(response.status_code)


def avoid_sslerror():
    """避免验证错误"""
    response = requests.get('https://www.zimuku.la', verify=False)
    print(response.status_code)


def ignore_warning():
    """避免错误同时忽略警告"""
    urllib3.disable_warnings()
    response = requests.get('https://www.zimuku.la', verify=False)
    print(response.status_code)


def catch_warning():
    """避免错误捕获警告"""
    logging.captureWarnings(True)
    response = requests.get('https://www.zimuku.la', verify=False)
    print(response.status_code)


def install_crt():
    """或者直接指定一个本地证书用作客户端证书"""
    # 需要有 crt 和 key 文件，并且指定它们的路径。注意，本地私有证书的 key 必须是解密状态，加密状态的 key 是不支持的。
    response = requests.get('https://www.zimuku.la', cert=('/path/server.crt', '/path/key'))
    print(response.status_code)


if __name__ == '__main__':
    # sslerror()
    # 输出结果：
    # requests.exceptions.SSLError: ("bad handshake: Error([('SSL routines', 'tls_process_server_certificate',
    # 'certificate verify failed')])")

    # avoid_sslerror()
    # 输出结果：
    # /usr/lib/python3/dist-packages/urllib3/connectionpool.py:999: InsecureRequestWarning: Unverified
    # HTTPS request is being made to host 'www.zimuku.la'. Adding certificate verification is strongly
    # advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    #   warnings.warn(
    # 200

    ignore_warning()
    catch_warning()
