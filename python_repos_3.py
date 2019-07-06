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

#提取关于仓库名字，用星级，url和description自动生成字典，在绘图时导入，生成自定义工具提示
names, info_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    info_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),#不明白为什么要加str()?????
        'xlink': repo_dict['html_url'],
    }
    info_dicts.append(info_dict)

#可视化结果
my_style = LS('#449966', base_style = LCS)

#创建Config类的实例my_config，并设置属性
my_config = pygal.Config()
my_config.x_label_rotation = 43
my_config.show_legend = False
my_config.title_font_size = 26
my_config.label_font_size = 15
my_config.major_label_font_size = 19
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 800

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Most_Starred Python Projects on Github'
chart.x_labels = names

#传入字典列表info_dicts
chart.add('', info_dicts)
chart.render_to_file('python_repos_3.svg')