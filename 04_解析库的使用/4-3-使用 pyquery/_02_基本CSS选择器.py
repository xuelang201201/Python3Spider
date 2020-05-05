from pyquery import PyQuery as pq


html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">forth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)
print(doc('#container .list li'))  # 先选取 id 为 container 的节点，再选取其内部的 class 为 list 的节点内部的所有 li 节点。
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
print(type(doc('#container .list li')))
# <class 'pyquery.pyquery.PyQuery'>
