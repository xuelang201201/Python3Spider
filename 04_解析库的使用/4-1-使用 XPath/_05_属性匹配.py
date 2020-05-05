from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')  # 选取 class 为 item-0 的 li 节点
print(result)
# [<Element li at 0x7f01119d4900>, <Element li at 0x7f01119d4940>]
