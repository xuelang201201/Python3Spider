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
print(a, type(a))
# <a href="link3.html"><span class="bold">third item</span></a> <class 'pyquery.pyquery.PyQuery'>
print(a.attr('href'))
# link3.html
print(a.attr.href)
# link3.html

a = doc('a')
print(a, type(a))
# <a href="link2.html">second item</a><a href="link3.html"><span class="bold">third item</span></a><a
# href="link4.html">forth item</a><a href="link5.html">fifth item</a> <class 'pyquery.pyquery.PyQuery'>
print(a.attr('href'))
# link2.html
print(a.attr.href)
# link2.html

a = doc('a')
for item in a.items():
    print(item.attr('href'))
# link2.html
# link3.html
# link4.html
# link5.html
