import json
import subprocess

# JSON文件名
json_filename = 'data.json'
# 文本文件名
text_filename = 'gold_value.txt'

# 尝试读取和解析JSON文件
try:
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)
except json.decoder.JSONDecodeError as e:
    print(f"Error reading the JSON file: {e}")
    # 打印出问题的文件内容
    with open(json_filename, 'r') as json_file:
        print(json_file.read())
    exit(1)

# 尝试读取文本文件并更新JSON对象
try:
    with open(text_filename, 'r') as txt_file:
        gold_value = txt_file.read().strip()
    data['gold'] = gold_value
except FileNotFoundError:
    print(f"The file {text_filename} was not found.")
    exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

# 将更新后的JSON数据写回文件
try:
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
except IOError as e:
    print(f"An error occurred while writing to the JSON file: {e}")
    exit(1)

# 使用Git命令推送更改到GitHub仓库
try:
    # 添加更改到Git
    subprocess.run(['git', 'add', json_name], check=True)
    # 创建提交
    subprocess.run(['git', 'commit', '-m', 'Update gold value in JSON'], check=True)
    # 推送到远程仓库
    subprocess.run(['git', 'push'], check=True)
    print("Changes pushed to GitHub repository successfully.")
except subprocess.CalledProcessError as e:
    print("An error occurred while pushing changes to GitHub:", e)
