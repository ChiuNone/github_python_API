#编写一个使用web应用编程接口(API)自动请求网站特定信息而不是整个网页，再对这些信息进行可视化

#Web API是在网站的一部分，用于与使用非常具体的URL请求特定信息的程序交互。这种请求称为API调用。
#请求获得数据以json或者csv格式返回。

#本次编程项目基于来自github的信息，使用github的API请求有关该网站中python项目的信息
#然后使用pygal进行可视化，呈现这些项目的受欢迎程度

#使用API请求数据
#在浏览器中输入:https://api.github.com/search/repositories?q=language:python&sort=stars
#得到所有在github上的python项目及其相关信息。

#接下来处理API请求得到数据
#见repos.py，first_repos.py

#储存响应的数据并处理它
#见repos.py，first_repos.py

#处理好数据后，利用pygal可视化数据
#见python_repos.py

#改进图表样式，包括字体，样式等
#调整代码结构，创建一个配置对象，传递给Bar()
#见python_repos_2.py

#根据数据绘图，自定义工具提示
#工具提示：鼠标指向条形将显示除了星级以外还显示其他信息
#做法是向方法add()，添加一个字典列表而不是单一的值列表
#见python_repos_3.py
