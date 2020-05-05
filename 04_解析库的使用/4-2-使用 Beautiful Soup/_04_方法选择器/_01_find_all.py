import re

from bs4 import BeautifulSoup


"""(1) name
可以根据节点名来查询元素
"""
html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
# [<ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>, <ul class="list list-small" id="list-2">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# </ul>]
print(type(soup.find_all(name='ul')[0]))
# <class 'bs4.element.Tag'>

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
# [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
# [<li class="element">Foo</li>, <li class="element">Bar</li>]

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
# [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>]
# Foo
# Bar
# Jay
# [<li class="element">Foo</li>, <li class="element">Bar</li>]
# Foo
# Bar


"""(2) attrs
传入一些属性来查询
"""
html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(attrs={'id': 'list-1'}))
# [<ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>]
print(soup.find_all(attrs={'name': 'elements'}))
# [<ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>]

print(soup.find_all(id='list-1'))
# [<ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>]
print(soup.find_all(class_='element'))
# [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>,
# <li class="element">Foo</li>, <li class="element">Bar</li>]


"""(3) text
text 参数可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象
"""

html = '''
<div class="panel">
<div class="panel-body">
<a>Hello, this is a link</a>
<a>Hello, this is a link, too</a>
</div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))
# ['Hello, this is a link', 'Hello, this is a link, too']
