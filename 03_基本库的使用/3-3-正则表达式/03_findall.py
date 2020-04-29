import re

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
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
# [('/2.mp3', '任贤齐', '沧海一声笑'), ('/3.mp3', '齐秦', '往事随风'), ('/4.mp3', 'beyond', '光辉岁月'),
# ('/5.mp3', '陈慧琳', '记事本'), ('/6.mp3', '邓丽君', '但愿人长久')]
print(type(results))
# <class 'list'>
for result in results:
    print(result)
    print(result[0], result[1], result[2])
# ('/2.mp3', '任贤齐', '沧海一声笑')
# /2.mp3 任贤齐 沧海一声笑
# ('/3.mp3', '齐秦', '往事随风')
# /3.mp3 齐秦 往事随风
# ('/4.mp3', 'beyond', '光辉岁月')
# /4.mp3 beyond 光辉岁月
# ('/5.mp3', '陈慧琳', '记事本')
# /5.mp3 陈慧琳 记事本
# ('/6.mp3', '邓丽君', '但愿人长久')
# /6.mp3 邓丽君 但愿人长久
