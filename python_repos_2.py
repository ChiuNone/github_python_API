import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#调用API，存储返回对象
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code', r.status_code)

#处理返回对象
repo_date = r.json()
print(repo_date.keys())
print('Total repositories:', repo_date['total_count'])

repo_dicts = repo_date['items']
print('Repositories returned:', len(repo_dicts))

#提取关于仓库名字和星级的信息，绘制名字-星级
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#可视化结果
my_style = LS('#449966', base_style = LCS)

#创建Config类的实例my_config，并设置属性
my_config = pygal.Config()
my_config.x_label_rotation = 43
my_config.show_legend = False#图例显示设置
my_config.title_font_size = 26
my_config.label_font_size = 15#副标签字体大小
my_config.major_label_font_size = 19
my_config.truncate_label = 15#控制项目名字的字符在15个以内
my_config.show_y_guides = False#图表中水平点画虚线的显示设置
my_config.width = 800

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Most_Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos_2.svg')
