import json
import requests
import JSONDecodeError

# 假设这是你的GitHub仓库中文件的URL
url_json = 'https://raw.githubusercontent.com/xiaoji235/py-jump/main/data.json'
url_gold_value = 'https://raw.githubusercontent.com/xiaoji235/py-jump/main/gold_value.txt'

# 使用requests库从GitHub获取data.json内容
response_json = requests.get(url_json)

try:
    data = response_json.json()
except json.decoder.JSONDecodeError as e:
    print("Error decoding JSON from data.json:", e)
    exit()

# 使用requests库从GitHub获取gold_value内容
response_gold_value = requests.get(url_gold_value)
gold_value = response_gold_value.text.strip()  # 移除可能的空白字符

# 替换gold值
data['gold'] = gold_value

# 将更新后的JSON对象写入新的data.json文件
with open('new_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('Gold value has been updated in new_data.json.')
