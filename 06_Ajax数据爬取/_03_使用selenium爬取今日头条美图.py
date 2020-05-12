import time
import os
import re
import requests

from functools import partial
from hashlib import md5
from multiprocessing.pool import Pool
from selenium import webdriver


def get_cookies(url):
    s = ''
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    for i in browser.get_cookies():
        try:
            name = i.get('name')
            value = i.get('value')
            s = s + name + '=' + value + ';'
        except ValueError as e:
            print(e)
    return s


class GetCookie(object):
    def __init__(self, url):
        self.cookies = get_cookies(url)
        self.headers = {
            'cookie': self.cookies,
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'referer': 'https://www.toutiao.com/search/?keyword=%E5%86%99%E7%9C%9F',
        }

    def get_page(self, offset):
        params = {
            'aid': '24',
            'app_name': 'web_search',
            'offset': offset,
            'format': 'json',
            'keyword': '写真',
            'autoload': 'true',
            'count': '20',
            'en_qc': '1',
            'cur_tab': '1',
            'from': 'search_tab',
            'pd': 'synthesis',
        }
        url = 'https://www.toutiao.com/api/search/content/'
        try:
            r = requests.get(url, params=params, headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                print('Requests get page error!')
        except requests.ConnectionError:
            return None

    def get_images(self, json):
        data = json.get('data')
        if data:
            for i in data:
                if i.get('title'):
                    title = re.sub('[\t]', '', i.get('title'))
                    url = i.get('article_url')
                    if url:
                        r = requests.get(url, headers=self.headers)
                        if r.status_code == 200:
                            images_pattern = re.compile(r'JSON.parse\("(.*?)"\),\n', re.S)
                            result = re.search(images_pattern, r.text)
                            if result:
                                b_url = 'http://p3.pstatp.com/origin/pgc-image/'
                                up = re.compile(r'url(.*?)"width', re.S)
                                results = re.findall(up, result.group(1))
                                if results:
                                    for result in results:
                                        yield {
                                            'title': title,
                                            'image': b_url + re.search('F([^F]*)\\\\",', result).group(1)
                                        }
                            else:
                                images = i.get('image_list')
                                for image in images:
                                    origin_image = re.sub("list.*?pgc-image", "large/pgc-image",
                                                          image.get('url'))  # 改成 origin/pgc-image 是原图
                                    yield {
                                        'image': origin_image,
                                        'title': title
                                    }


def save_image(item):
    img_path = 'img' + os.path.sep + ''.join(
        re.findall(r'[\u4e00-\u9fa5a-zA-Z0-9]+', item.get('title'), re.S))  # 去除不能作为文件名的字符
    if not os.path.exists(img_path):
        os.makedirs(img_path)  # 生成目录文件夹
    try:
        resp = requests.get(item.get('image'))
        if requests.codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')  # 单一文件的路径
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print(e, 'none123')


def main(offset, get_cookie):
    a = get_cookie.get_page(offset)
    for i in get_cookie.get_images(a):
        save_image(i)


if __name__ == '__main__':
    start = time.perf_counter()
    get_cookie = GetCookie('https://www.toutiao.com')
    p_work = partial(main, get_cookie=get_cookie)
    p = Pool()
    groups = [x * 20 for x in range(0, 3)]
    p.map(p_work, groups)
    end = time.perf_counter()
    print('Running Time: ' + str(end - start) + 's')
