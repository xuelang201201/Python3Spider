import http.cookiejar, urllib.request


def print_cookies():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + " = " + item.value)


def save_cookies():
    # 输出成文件格式
    filename = 'cookies.txt'
    # cookie = http.cookiejar.MozillaCookieJar(filename)
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


def load_cookies():
    # 从文件中读取并利用
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookies.txt', ignore_expires=True, ignore_discard=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    # print_cookies()
    # save_cookies()
    load_cookies()
