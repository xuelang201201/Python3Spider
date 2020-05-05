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
# 单个节点，可以直接打印输出，也可以直接转成字符串
li = doc('.item-0.active')
print(li)
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
print(str(li))
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>

# 多个节点，需要遍历来获取
lis = doc('li').items()
print(type(lis))
# <class 'generator'>
for li in lis:
    print(li, type(li))
# <li class="item-0">first item</li>
#  <class 'pyquery.pyquery.PyQuery'>
# <li class="item-1"><a href="link2.html">second item</a></li>
#  <class 'pyquery.pyquery.PyQuery'>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#  <class 'pyquery.pyquery.PyQuery'>
# <li class="item-1 active"><a href="link4.html">forth item</a></li>
#  <class 'pyquery.pyquery.PyQuery'>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
#  <class 'pyquery.pyquery.PyQuery'>
