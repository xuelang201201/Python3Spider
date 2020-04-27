from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

# 运行结果：
# http://www.baidu.com/FAQ.html
# https://cuiqingcai.com/FAQ.html
# https://cuiqingcai.com/FAQ.html
# https://cuiqingcai.com/FAQ.html?question=2
# https://cuiqingcai.com/index.php
# http://www.baidu.com?category=2#comment
# www.baidu.com?category=2#comment
# www.baidu.com?category=2

"""
可以发现，base_url 提供了三项内容 scheme、netloc 和 path。如果这 3 项在新的链接里不存在，
就予以补充；如果新的链接存在，就使用新的链接的部分。而 base_url 中的 params、query 和 fragment
是不起作用的。
"""
