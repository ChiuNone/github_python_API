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

#可视化
my_style = LS('#336666', base_style = LCS)
chart = pygal.Bar(style = my_style, x_label_rotation = 36, show_legend = False)
chart.title = 'Most_Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('pythhon_repos.svg')