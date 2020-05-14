import requests

from urllib.parse import quote


def render_html():
    """render.html
    此接口用于获取 JavaScript 渲染的页面的 HTML 代码，接口地址就是 Splash 的运行地址家此接口名称，
    例如：http://localhost:8050/render.html
    """
    url = 'http://localhost:8050/render.html?url=https://www.baidu.com'
    response = requests.get(url)
    print(response.text)

    # 此接口还可以指定其他参数，比如通过 wait 指定等待秒数。
    url = 'http://localhost:8050/render.html?url=https://www.taobao.com&wait=5'
    response = requests.get(url)
    print(response.text)


def render_png():
    """render.png
    此接口可以获取网页截图
    """
    url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
    response = requests.get(url)
    with open('jd.png', 'wb') as f:
        f.write(response.content)


def render_jpeg():
    """render.jpeg
    quality 参数默认值为 75，范围在 0-100，应该避免高于 95
    """
    url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700&quality=90'
    response = requests.get(url)
    with open('jd.jpeg', 'wb') as f:
        f.write(response.content)


def render_har():
    """render.har
    用于获取页面加载的 HAR 数据
    """
    url = 'http://localhost:8050/render.har?url=https://www.jd.com&wait=5'
    response = requests.get(url)
    print(response.text)


def render_json():
    """render.json
    此接口包含了前面接口的所有功能
    :return: 返回结果是 JSON 格式
    """
    url = 'http://localhost:8050/render.json?url=https://www.baidu.com'
    # url = 'http://localhost:8050/render.json?url=https://www.baidu.com&html=1&har=1'
    response = requests.get(url)
    print(response.text)


def execute():
    """此接口才是最强大的接口，可实现一些交互操作
    """
    lua = '''
    function main(splash)
        return 'hello'
    end
    '''

    url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
    response = requests.get(url)
    print(response.text)

    lua = '''
    function main(splash, args)
        local treat = require("treat")
        local response = splash:http_get("http://httpbin.org/get")
            return {
                html=treat.as_string(response.body),
                url=response.url,
                status=response.status
            }
    end
    '''

    url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
    response = requests.get(url)
    print(response.text)


def main():
    # render_html()
    # render_png()
    # render_jpeg()
    # render_har()
    # render_json()
    execute()


if __name__ == '__main__':
    main()
