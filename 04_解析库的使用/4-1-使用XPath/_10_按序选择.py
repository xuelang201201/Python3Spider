from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')  # 选取了第一个 li 节点，中括号传入数字 1 即可。
print(result)
result = html.xpath('//li[last()]/a/text()')  # 选取了最后一个 li 节点，中括号中传入 last() 即可。
print(result)
result = html.xpath('//li[position()<3]/a/text()')  # 选取了位置小于 3 的 li 节点，也就是位置序号为 1 和 2 的节点。
print(result)
result = html.xpath('//li[last()-2]/a/text()')  # 选取了倒数第三个 li 节点，中括号中传入 last()-2 即可。
print(result)
