from pyquery import PyQuery as pq

html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">forth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
li = doc('li:first-child')  # 第一个 li 节点
print(li)
# <li class="item-0">first item</li>
li = doc('li:last-child')  # 最后一个 li 节点
print(li)
# <li class="item-0"><a href="link5.html">fifth item</a></li>
li = doc('li:nth-child(2)')  # 第二个 li 节点
print(li)
# <li class="item-1"><a href="link2.html">second item</a></li>
li = doc('li:gt(2)')  # 第三个 li 之后的 li 节点
print(li)
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
li = doc('li:nth-child(2n)')  # 偶数位置的 li 节点
print(li)
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
li = doc('li:contains(second)')  # 包含 second 文本的 li 节点
print(li)
# <li class="item-1"><a href="link2.html">second item</a></li>
