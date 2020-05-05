from lxml import etree

# 最后一个 li 节点是没有闭合的，但是 etree 模块可以自动修正 HTML 文本。
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)  # bytes 类型
result = etree.tostring(html)  # tostring 转换成 str 类型
print(result.decode('utf-8'))
# 输出结果：
# <html><body><div>
# <ul>
# <li class="item-0"><a href="link1.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </li></ul>   # li 节点标签被补全
# </div>
# </body></html>  # 并且还自动添加了 body、html 节点。

# 直接读取文件内容进行解析
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
# 输出结果，多了一个 DOCTYPE 的声明，不过对解析无任何影响：
# <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
# <html><body><div>
# <ul>
# <li class="item-0"><a href="link1.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </li></ul>
# </div></body></html>
