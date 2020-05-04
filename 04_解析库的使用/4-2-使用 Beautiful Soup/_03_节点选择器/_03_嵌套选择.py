from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
# <title>The Dormouse's story</title>
print(type(soup.head.title))
# <class 'bs4.element.Tag'>
print(soup.head.title.string)
# The Dormouse's story
