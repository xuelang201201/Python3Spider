Robots 协议也称作爬虫协议、机器人协议，它的全名叫作网络爬虫排除标准（Robots Exclusion Protocol），
用来告诉爬虫和搜索引擎哪些页面可以抓取，哪些不可以抓取。它通常是一个叫做 robots.txt 的文本条件，一般
放在网站的根目录下。     

robots.txt 的样例：  
````
   User-agent: *
   Disallow: /
   Allow: /public/
````
这实现了对所有搜索爬虫只允许爬取 public 目录的功能，将上述内容保存成 robots.txt 文件，放在
网站的根目录下，和网站的入口文件（比如 index.php、index.html 和 index.jsp 等）放在一起。

上面的 User-agent 描述了搜索爬虫的名称，这里将其设置为 * 则代表该协议对任何爬取爬虫有效。
比如，可以设置：
```
    User-agent: Baiduspider
```
这就表示我们设置的规则对百度爬虫是有效的。如果有多条 User-agent 记录，则就会有多个爬虫会受到爬取限制，
但至少需要指定一条。

Disallow 指定了不允许抓取的目录，比如上例子中设置为 / 则代表不允许抓取所有页面。

Allow 一般和 Disallow 一起使用，一般不会单独使用，用来排除某些限制。现在设置为 /public/，
则表示所有页面不允许抓取，但可以抓取 public 目录。

禁止所有爬虫访问任何目录的代码：
```
    User-agent: *
    Disallow: /
```

允许所有爬虫访问任何目录的代码：
```
    User-agent: *
    Disallow:
```

另外，直接把 robots.txt 文件留空也是可以的。

禁止所有爬虫访问网站某些目录的代码：
```
    User-agent: *
    Disallow: /private/
    Disallow: /tmp/
```

只允许某一个爬虫访问的代码：
```
    User-agent: WebCrawler
    Disallow:
    User-agent: *
    Disallow: /
```
这些是 robots.txt 的一些常见写法。
