from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
# ['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
