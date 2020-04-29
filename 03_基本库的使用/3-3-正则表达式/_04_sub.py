"""使用 sub 修改文本"""

import re

content = '54aK54yA5oiR54ix5L2g'
content = re.sub(r'\d+', '', content)
print(content)
# aKyAoiRixLg

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''
results = re.findall(r'<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)  # 繁琐
for result in results:
    print(result[1])
# 一路上有你
# 沧海一声笑
# 往事随风
# 光辉岁月
# 记事本
# 但愿人长久

html = re.sub('<a.*?>|</a>', '', html)  # 使用 sub 就很简单
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
for result in results:
    print(result.strip())
# <div id="songs-list">
# <h2 class="title">经典老歌</h2>
# <p class="introduction">
# 经典老歌列表
# </p>
# <ul id="list" class="list-group">
# <li data-view="2">一路上有你</li>
# <li data-view="7">
# 沧海一声笑
# </li>
# <li data-view="4" class="active">
# 往事随风
# </li>
# <li data-view="6">光辉岁月</li>
# <li data-view="5">记事本</li>
# <li data-view="5">
# 但愿人长久
# </li>
# </ul>
# </div>
# 一路上有你
# 沧海一声笑
# 往事随风
# 光辉岁月
# 记事本
# 但愿人长久
