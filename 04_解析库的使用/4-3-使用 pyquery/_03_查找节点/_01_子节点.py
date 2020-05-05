from pyquery import PyQuery as pq

html = '''
<div>
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
items = doc('.list')
print(type(items))
# <class 'pyquery.pyquery.PyQuery'>
print(items)
# <ul class="list">
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
lis = items.find('li')  # 所有子孙节点
print(type(lis))
# <class 'pyquery.pyquery.PyQuery'>
print(lis)
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>

lis = items.children()  # 字节点
print(type(lis))
# <class 'pyquery.pyquery.PyQuery'>
print(lis)
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>

lis = items.children('.active')
print(lis)
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
