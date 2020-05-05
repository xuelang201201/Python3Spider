"""通过 / 或 // 即可查找元素的字节点或子孙节点
"""
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')  # 选择所有 li 节点的所有直接 a 子节点
print(result)
# [<Element a at 0x7f18beb09980>, <Element a at 0x7f18beb099c0>, <Element a at 0x7f18beb09a00>,
# <Element a at 0x7f18beb09a40>, <Element a at 0x7f18beb09a80>]

result = html.xpath('//ul//a')  # 获取 ul 节点下的所有子孙 a 节点，使用 //ul/a 无法获取
print(result)
# [<Element a at 0x7f18beb09980>, <Element a at 0x7f18beb099c0>, <Element a at 0x7f18beb09a00>,
# <Element a at 0x7f18beb09a40>, <Element a at 0x7f18beb09a80>]
