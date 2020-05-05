from pyquery import PyQuery as pq


html = '''
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
li.attr('name', 'link')
print(li)
# <li class="item-0 active" name="link"><a href="link3.html"><span class="bold">third item</span></a></li>
li.text('changed item')
print(li)
# <li class="item-0 active" name="link">changed item</li>
li.html('<span>changed item</span>')
print(li)
# <li class="item-0 active" name="link"><span>changed item</span></li>
