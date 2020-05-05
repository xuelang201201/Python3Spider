from bs4 import BeautifulSoup


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
print(soup.select('.panel .panel-heading'))
# [<div class="panel-heading">
# <h4>Hello</h4>
# </div>]
print(soup.select('ul li'))
# [<li class="element">Foo</li>, <li class="element">Bar</li>, <li class="element">Jay</li>,
# <li class="element">Foo</li>, <li class="element">Bar</li>]
print(soup.select('#list-2 .element'))
# [<li class="element">Foo</li>, <li class="element">Bar</li>]
print(type(soup.select('ul')[0]))
# <class 'bs4.element.Tag'>
