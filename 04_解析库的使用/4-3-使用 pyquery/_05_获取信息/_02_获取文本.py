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
a = doc('.item-0.active a')
print(a)
# <a href="link3.html"><span class="bold">third item</span></a>
print(a.text())
# third item

li = doc('.item-0.active')
print(li)
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
print(li.html())
# <a href="link3.html"><span class="bold">third item</span></a>


html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">forth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
li = doc('li')
print(li.html())
# <a href="link2.html">second item</a>
print(li.text())
# second item third item forth item fifth item
print(type(li.text()))
# <class 'str'>
