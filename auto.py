import json
import os

# 使用curl命令获取远程JSON数据
json_data = os.popen('curl -s <URL_OF_JSON>').read()

# 将JSON数据转换为Python字典
data_dict = json.loads(json_data)

# 获取rank为1的gold值
gold_value = data_dict['data']['rank'][1]['gold']

# 将gold值输出到文件
with open('gold_value.txt', 'w') as file:
    file.write(str(gold_value))

# 打印gold值
print(f"Gold值为: {gold_value}")

# 将gold值提交到仓库
os.system('git add gold_value.txt')
os.system('git commit -m "Update gold value"')
os.system('git push')
