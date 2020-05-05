from pyquery import PyQuery as pq

html = '''
<div class="wrap">
    Hello, World
<p>This is a paragraph.</p>
</div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
# Hello, World This is a paragraph.
wrap.find('p').remove()
print(wrap.text())
# Hello, World
