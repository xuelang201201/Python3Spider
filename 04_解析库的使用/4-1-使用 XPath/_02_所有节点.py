from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')  # 使用 // 开头的 XPath 规则来选取所有的符合要求的节点。使用 * 匹配所有的节点。
print(result)
# 输出结果：所有节点都被获取了。
# [<Element html at 0x7f7a75dc1800>, <Element body at 0x7f7a75dc18c0>, <Element div at 0x7f7a75dc1900>,
# <Element ul at 0x7f7a75dc1940>, <Element li at 0x7f7a75dc1980>, <Element a at 0x7f7a75dc1a00>, <Element
# li at 0x7f7a75dc1a40>, <Element a at 0x7f7a75dc1a80>, <Element li at 0x7f7a75dc1ac0>, <Element a at
# 0x7f7a75dc19c0>, <Element li at 0x7f7a75dc1b00>, <Element a at 0x7f7a75dc1b40>, <Element li at
# 0x7f7a75dc1b80>, <Element a at 0x7f7a75dc1bc0>]

# 匹配指定节点名称
result = html.xpath('//li')
print(result)
# [<Element li at 0x7fe893c20b00>, <Element li at 0x7fe893c20bc0>, <Element li at 0x7fe893c20c40>,
# <Element li at 0x7fe893c20c80>, <Element li at 0x7fe893c20d00>]
print(result[0])
# <Element li at 0x7fe893c20b00>
