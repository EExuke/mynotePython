# 编写自动下载数据并对其进行可视化的程序。

# 3、使用API
	Web API
	Pygal可视化仓库
	Hacker News API

# Web API:
		Web API 是网站的一部分,用于与使用非常具体的 URL 请求特定信息的程序交互。这种请求称为 API 调用。
	请求的数据将以易于处理的格式(如 JSON 或 CSV )返回。
	依赖于外部数据源的大多数应用程序都依赖于 API 调用,如集成社交媒体网站的应用程序。

	[ https://api.github.com/search/repositories?q=language:python&sort=stars ]

	这个调用返回 GitHub 当前托管了多少个 Python 项目,还有有关最受欢迎的 Python 仓库的信息。下面来仔细研究这个调用。
	第一部分( https://api.github.com/ ):
		将请求发送到 GitHub 网站中响应 API 调用的部分;
	接下来的一部分( search/repositories ):
		让 API 搜索 GitHub 上的所有仓库。
	repositories 后面的问号指出我们要传递一个实参。 
	q 表示查询,而等号让我们能够开始指定查询( q= )。
	通过使用 language:python ,我们指出只想获取主要语言为Python 的仓库的信息。
	最后一部分( &sort=stars )指定将项目按其获得的星级进行排序。

		requests 包让 Python 程序能够轻松地向网站请求信,息以及检查返回的响应:
	$ pip3 install --user requests

		在 Hacker News 网站,用户分享编程和技术方面的文章,并就这些文章展开积极的讨论。
	Hacker News 的 API 让你能够访问有关该网站所有文章和评论的信息,且不要求你通过注册获得密钥。
	[ https://hacker-news.firebaseio.com/v0/item/9884165.json ]
