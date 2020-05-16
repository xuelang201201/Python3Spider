def firefox():
    proxy = '120.79.139.253:8080'
    options = webdriver.FirefoxOptions()
    options.add_argument('--proxy-server=http://' + proxy)
    firefox_browser = webdriver.Firefox(options=options)
    firefox_browser.get('http://httpbin.org/get')


def chrome():
    """一般方法"""

    global browser

    proxy = '120.79.139.253:8080'
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=http://' + proxy)
    browser = webdriver.Chrome(options=options)
    browser.get('http://httpbin.org/get')


def chrome_with_verify():
    """代理设置方法"""

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import zipfile

    global browser

    ip = '127.0.0.1'
    port = 9743
    username = 'foo'
    password = 'bar'

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"            
        ],
        "background": {
            "scripts": ["background.js"]
        }
    }
    """

    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "%(ip)s",
                port: %(port)s
            }
        }
    }
    
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
    
    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%(username)s",
                password: "%(password)s"
            }
        }
    }
    
    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {urls: ["<all_urls>"]},
        ['blocking']
    )
    """ % {'ip': ip, 'port': port, 'username': username, 'password': password}

    plugin_file = 'proxy_auth_plugin.zip'
    with zipfile.ZipFile(plugin_file, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    options = Options()
    options.add_argument("--start-maximized")
    options.add_extension(plugin_file)
    browser = webdriver.Chrome(options=options)
    browser.get('http://httpbin.org/get')


def headless():
    """无界面设置方法"""

    from selenium import webdriver

    service_args = [
        '--proxy=120.79.139.253:8080',
        '--proxy-type=http',
        # '--proxy-auth=username:password'  # 如果需要认证，加入这一行代码即可
    ]
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(service_args=service_args, options=options)
    browser.get('http://httpbin.org/get')
    print(browser.page_source)


if __name__ == '__main__':
    from selenium import webdriver

    # firefox()
    # chrome()
    # chrome_with_verify()
    headless()
