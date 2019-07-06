import requests

#执行API调用并储存返回的数据
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)
#返回的数据或者说响应的对象包含一属性：status_code，表示API调用请求是否成功

#将API返回的数据储存在一个变量中
response_dict = r.json()

print(response_dict.keys())
print('Total python repositories:', response_dict['total_count'])

#处理响应字典
#返回数据中键items的值是一个列表，列表中每个对象是一个关于仓库相关信息的字典。
repo_dicts = response_dict['items']
print('repositories returned:', len(repo_dicts))#获悉获得几个仓库的信息

#查看第一个仓库的信息
repo_dict = repo_dicts[0]
print('keys:', len(repo_dict.keys()))
for key in sorted(repo_dict.keys()):
    print(key)

print('\nSelected information about first repository:')
print('Nmane:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Description:', repo_dict['description'])


