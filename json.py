import json
import os
import requests
import subprocess

# JSON文件名
json_filename = 'data.json'
# 文本文件名
text_filename = 'gold_value.txt'

# 读取JSON文件
with open(json_filename, 'r') as json_file:
    data = json.load(json_file)

# 读取gold_value.txt文件来获取gold值
with open(text_filename, 'r') as txt_file:
    gold_value = txt_file.read().strip()

# 更新JSON数据中的gold字段
data['gold'] = gold_value

# 将更新后的JSON数据写回文件
with open(json_filename, 'w') as json_file:
    json.dump(data, json_file, indent=4)

# 使用Git命令推送更改到GitHub仓库
try:
    # 添加更改到Git
    subprocess.run(['git', 'add', json_filename], check=True)
    # 创建提交
    subprocess.run(['git', 'commit', '-m', 'Update gold value in JSON'], check=True)
    # 推送到远程仓库
    subprocess.run(['git', 'push'], check=True)
    print("Changes pushed to GitHub repository successfully.")
except subprocess.CalledProcessError as e:
    print("An error occurred while pushing changes to GitHub:", e)
