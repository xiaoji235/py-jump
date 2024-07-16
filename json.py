import json
import os
import requests

# 假设你有以下JSON字符串
json_str = '{"gameId":"10005","gold":"xxx","hasPass":true,"gameLogId":"1813145167239188480"}'

# 将JSON字符串解析为字典
data = json.loads(json_str)

# 将新的gold值转回为字符串，并更新字典
data['gold'] = str(gold_value)

# 如果需要将更新后的字典转回JSON字符串
new_json_str = json.dumps(data)

# 将新的JSON数据保存到文件
with open('updated_data.json', 'w') as file:
    file.write(new_json_str)

# 提交新的JSON文件到GitHub仓库
url = 'https://api.github.com/repos/xiaoji235/py-jump/contents/updated_data.json'
token = os.getenv('GITHUB_TOKEN')
headers = {'Authorization': f'token {token}'}
payload = {
    'message': 'Update gold value in JSON',
    'content': new_json_str
}
response = requests.put(url, headers=headers, json=payload)

print(response.text)
