import os
import requests
import re
import random

from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    headers = {
        'cookie': 'tt_webid=6825873911596779022; s_v_web_id=verify_ka3nw12e_8GBb7f4y_vMoR_4EFj_BViv_cEApHn4BuVZ2; '
                  'WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=nolhinffk1589272629828; tt_webid=6825873911596'
                  '779022; csrftoken=c4346b93a395a6ae44262176d29185b9; ttcid=c77d7bf9a28145e198ac78236201be3526;'
                  ' SLARDAR_WEB_ID=dfd394c6-be6b-48d1-9cac-55dcd4132d09; __ac_nonce=05eba605e0011987092bb; __ac_si'
                  'gnature=tuQB8gAgEBC-vnIdLQlj5rblAOAAOhsZdqQ81ebIoZc3gRDzZfqeKa9.jOI2b44.8rpteSOd6hU67Snyo4s-Qhz'
                  'i-rt.BFsaeYfe9QqUxlGlfwmOsRIFfHRMolXdcK9ZV4W; tt_scid=FqtfY2CM6rgAiJGBzPm46u-2wlL1vAjqgV0Ykntmkm'
                  'VwmlTaEUCJ3mqJ.MUkVLbha88d',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    }
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    base_url = 'http://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    global images
    headers = {
        'cookie': 'tt_webid=6825873911596779022; s_v_web_id=verify_ka3nw12e_8GBb7f4y_vMoR_4EFj_BViv_cEApHn4BuVZ2; '
                  'WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=nolhinffk1589272629828; tt_webid=6825873911596'
                  '779022; csrftoken=c4346b93a395a6ae44262176d29185b9; ttcid=c77d7bf9a28145e198ac78236201be3526;'
                  ' SLARDAR_WEB_ID=dfd394c6-be6b-48d1-9cac-55dcd4132d09; __ac_nonce=05eba605e0011987092bb; __ac_si'
                  'gnature=tuQB8gAgEBC-vnIdLQlj5rblAOAAOhsZdqQ81ebIoZc3gRDzZfqeKa9.jOI2b44.8rpteSOd6hU67Snyo4s-Qhz'
                  'i-rt.BFsaeYfe9QqUxlGlfwmOsRIFfHRMolXdcK9ZV4W; tt_scid=FqtfY2CM6rgAiJGBzPm46u-2wlL1vAjqgV0Ykntmkm'
                  'VwmlTaEUCJ3mqJ.MUkVLbha88d',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    }
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('title') is None:  # 刨掉前半部分无关内容
                continue
            title = re.sub('[\t]', '', item.get('title'))  # 获取标题
            url = item.get("article_url")  # 获取子链接
            if url is None:
                continue
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    images_pattern = re.compile(r'JSON.parse\("(.*?)"\),\n', re.S)
                    result = re.search(images_pattern, response.text)
                    if result is None:  # 非图集形式
                        images = item.get('image_list')
                        for image in images:
                            # 改成origin/pgc-image是原图
                            origin_image = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))
                            yield {
                                'image': origin_image,
                                'title': title
                            }
                    else:  # 图集形式，抓取 gallery 下 json 格式数据
                        url_pattern = re.compile('url(.*?)"width', re.S)
                        results = re.findall(url_pattern, result.group(1))
                        for i in range(len(results)):
                            yield {
                                # 存储url
                                'image': "http://p%d.pstatp.com/origin/pgc-image/" % (random.randint(1, 10)) +
                                         result1[i][result1[i].rindex("u002F") + 5:result1[i].rindex('\\"')],
                                'title': title
                            }
            except requests.ConnectionError:  # 打开子链接失败直接保存图集中的前半部分
                for image in images:
                    # 改成 origin/pgc-image 是原图
                    origin_image = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))
                    yield {
                        'image': origin_image,
                        'title': title
                    }


def save_image(item):
    image_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(image_path):
        os.mkdir(image_path)  # 生成目录文件夹
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = image_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(response.content).hexdigest(), file_suffix='jpg')  # 单一文件的路径
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(0, 3)])
    pool.map(main, groups)
    # pool.close()
    # pool.join()
