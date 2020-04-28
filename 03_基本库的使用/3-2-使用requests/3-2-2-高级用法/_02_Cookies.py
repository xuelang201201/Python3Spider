"""使用 requests 获取和设置 Cookies"""

import requests


def get_cookies():
    r = requests.get("https://www.baidu.com")
    print(r.cookies)
    for key, value in r.cookies.items():
        print(key + '=' + value)


def use_cookie_login1():
    headers = {
        'Cookie': '_zap=81f37ca5-2f76-4258-9ce4-c94c3a58a223; d_c0="ACAda3awExGPTuB6Hkz9h89AhP1MUBJtkh4=|1586159103";'
                  ' _ga=GA1.2.283633685.1586159105; capsion_ticket="2|1:0|10:1586159112|14:capsion_ticket|44:YWQxMDI'
                  '2MTlhNTY0NDUzMDllNGU5NTEyMzNiMzNmZDk=|d5115737d25b12223a6d8a3f82468c8ec7e5ace643b903cd90ccd81e13c'
                  '0ea25"; z_c0="2|1:0|10:1586159131|4:z_c0|92:Mi4xODlmYkF3QUFBQUFBSUIxcmRyQVRFU1lBQUFCZ0FsVk5HeXg0W'
                  'HdBbkktUTVIOThmM0R5VGlTTF9leHJHS1FIWkh3|c4279059a49f833796d6b69eafdbf12726318f420a1b937afa09a6698'
                  '37524ee"; q_c1=92b3cfdfee7b4e6082d83f35a1dcf37a|1587379813000|1587379813000; tshl=; tst=r; _xsrf='
                  '8c79f0ac-0123-4d32-a5e6-9948ea56032e; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1587727946,158801137'
                  '0,1588012084,1588112296; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1588112296; _gid=GA1.2.96614705'
                  '4.1588112296; SESSIONID=9hYRtEpEhrUy2FEiTkzItyFEVyezWEYZ6RQ82JJKolj; JOID=W1AXAE6N-aIpmqiPRIdUMmj'
                  'TabJetZv6feLs9QDpiv1RruLLJy9ZDX2Xo4RDEdXy60GjJqQ7woqy-608RgosTpg=; osd=VVwWB02D9aMumaaDRYBXPGTSbr'
                  'FQuZr9fuzg9AfqhPFQqeHFKy5eDnObooNAH9nz7EKtKqU8wYS--qo_SAYtSZs=; KLBRSID=76ae5fb4fba0f519d97e594f1'
                  'cef9fab|1588112585|1588112294',
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com', headers=headers)
    print(r.text)


def use_cookie_login2():
    cookies = '''
    _zap=81f37ca5-2f76-4258-9ce4-c94c3a58a223; d_c0="ACAda3awExGPTuB6Hkz9h89AhP1MUBJtkh4=|1586159103";
     _ga=GA1.2.283633685.1586159105; capsion_ticket="2|1:0|10:1586159112|14:capsion_ticket|44:YWQxMDI
    2MTlhNTY0NDUzMDllNGU5NTEyMzNiMzNmZDk=|d5115737d25b12223a6d8a3f82468c8ec7e5ace643b903cd90ccd81e13c
    0ea25"; z_c0="2|1:0|10:1586159131|4:z_c0|92:Mi4xODlmYkF3QUFBQUFBSUIxcmRyQVRFU1lBQUFCZ0FsVk5HeXg0W
    HdBbkktUTVIOThmM0R5VGlTTF9leHJHS1FIWkh3|c4279059a49f833796d6b69eafdbf12726318f420a1b937afa09a6698
    37524ee"; q_c1=92b3cfdfee7b4e6082d83f35a1dcf37a|1587379813000|1587379813000; tshl=; tst=r; _xsrf=
    8c79f0ac-0123-4d32-a5e6-9948ea56032e; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1587727946,158801137
    0,1588012084,1588112296; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1588112296; _gid=GA1.2.96614705
    4.1588112296; SESSIONID=9hYRtEpEhrUy2FEiTkzItyFEVyezWEYZ6RQ82JJKolj; JOID=W1AXAE6N-aIpmqiPRIdUMmj
    TabJetZv6feLs9QDpiv1RruLLJy9ZDX2Xo4RDEdXy60GjJqQ7woqy-608RgosTpg=; osd=VVwWB02D9aMumaaDRYBXPGTSbr
    FQuZr9fuzg9AfqhPFQqeHFKy5eDnObooNAH9nz7EKtKqU8wYS--qo_SAYtSZs=; KLBRSID=76ae5fb4fba0f519d97e594f1
    cef9fab|1588112585|1588112294
    '''
    jar = requests.cookies.RequestsCookieJar()
    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36'
    }
    for cookie in cookies.split(';'):
        key, value = cookie.split('=', 1)
        jar.set(key, value)
    r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
    print(r.text)


if __name__ == '__main__':
    # get_cookies()
    # use_cookie_login1()
    use_cookie_login2()
