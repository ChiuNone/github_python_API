import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code', r.status_code)

file = r.json()
print(file.keys())
print('Total repositories:', file['total_count'])

repo_dicts = file['items']
print('Repositories returned:', len(repo_dicts))

#打印每个仓库的信息，包括名字，星级，在github上的url，所有者，描述
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])#owner也是字典的键
    print('Stars:', repo_dict['stargazers_count'])
    print('URL:', repo_dict['html_url'])
    print('Decription:', repo_dict['decription'])

