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
li = doc('.list .item-0.active')  # 选择 class 为 list 的节点内部 class 为 item-0 和 active 的节点
print(li.siblings())
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0">first item</li>
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>

print(li.siblings('.active'))  # class 为 active 的兄弟节点
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
