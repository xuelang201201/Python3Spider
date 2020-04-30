from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result)
# ['\n']

result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
# ['first item', 'fifth item']

result = html.xpath('//li[@class="item-0"]//text()')
print(result)
# ['first item', 'fifth item', '\n']
