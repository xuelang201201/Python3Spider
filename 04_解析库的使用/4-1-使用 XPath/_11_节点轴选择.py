from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
# 第一次选择时，调用了 ancestor 轴，可以获取所有祖先节点。其后需要跟两个冒号，
# 然后是节点的选择器，这里直接使用 *，表示匹配所有节点。
result = html.xpath('//li[1]/ancestor::*')
print(result)
# [<Element html at 0x7fdf5e002a40>, <Element body at 0x7fdf5d4fe5c0>, <Element div at 0x7fdf5d4fe680>,
# <Element ul at 0x7fdf5d4fe6c0>]
result = html.xpath('//li[1]/ancestor::div')  # 加上限定条件，得到的结果只有 div 这个祖先节点。
print(result)
# [<Element div at 0x7fdf5d4fe680>]
# 调用 attribute 轴，可以获取所有属性值，其后跟的选择器还是 *，代表获取节点的所有属性，返回值就是 li 节点的所有属性值。
result = html.xpath('//li[1]/attribute::*')
print(result)
# ['item-0']
# 调用了 child 轴，可以获取所有直接子节点。加上限定条件，选取 href 属性为 link1.html 的 a 节点。
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
# [<Element a at 0x7fdf5d4fe680>]
# 调用了 descendant 轴，可以获取所有子孙节点。加上限定条件选取 span 节点，所有返回的结果只包含 span 节点而不包含 a 节点。
result = html.xpath('//li[1]/descendant::span')
print(result)
# [<Element span at 0x7fdf5d4fe780>]
# 调用了 following 轴，可以获取当前节点之后的所有节点。虽然使用的是 * 匹配，但又加了索引选择，所以只获取了第二个后续节点。
result = html.xpath('//li[1]/following::*[2]')
print(result)
# [<Element a at 0x7fdf5d4fe740>]
# 调用了 following-sibling 轴，可以获取当前节点之后的所有同级节点。使用 * 匹配，所以获取了所有后续同级节点。
result = html.xpath('//li[1]/following-sibling::*')
print(result)
# [<Element li at 0x7fdf5d4fe540>, <Element li at 0x7fdf5d4fe680>, <Element li at 0x7fdf5d4fe5c0>,
# <Element li at 0x7fdf5d4fe6c0>]
