from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
# ['item-1']

result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
# ['item-1']
