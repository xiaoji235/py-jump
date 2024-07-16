import json
import os

# 使用curl命令获取远程JSON数据
json_data = os.popen("curl -s 'VP_SESSION_ID=6513ba65219d4ea6a81965af7997c1ae&Hm_lvt_42cc1880011538681c48bfa0eb27dee2=1720968508' -H 'Host: eastroc.lokwork.com' -H 'Accept: */*' -H 'Sec-Fetch-Site: same-origin' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh-Hans;q=0.9' -H 'Sec-Fetch-Mode: cors' -H 'Content-Type: application/json;' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.33(0x18002129) NetType/WIFI Language/zh_CN miniProgram/wxa16478da92a9df9b' -H 'Connection: keep-alive' -H 'Referer: https://eastroc.lokwork.com/leap/index.html?gameId=10005' -H 'Cookie: VP_SESSION_ID=6513ba65219d4ea6a81965af7997c1ae; Hm_lvt_42cc1880011538681c48bfa0eb27dee2=1720968508' -H 'Sec-Fetch-Dest: empty' 'https://eastroc.lokwork.com/eastroc-api/web/charmingLeap/getRankByPage?gameId=10005&pageNum=1&pageSize=10'").read()

# 将JSON数据转换为Python字典
data_dict = json.loads(json_data)

# 获取rank为1的gold值
gold_value = data_dict['data']['rank'][1]['gold']
gold_value += 1

# 将gold值输出到文件
with open('gold_value.txt', 'w') as file:
    file.write(str(gold_value))

# 打印gold值
print(f"Gold值为: {gold_value}")

# 将gold值提交到仓库
os.system('git add gold_value.txt')
os.system('git commit -m "Update gold value"')
os.system('git push')

#######gold值输出######

# 假设你有以下JSON字符串
json_str = '{"gameId":"10005","gold":"xxx","hasPass":true,"gameLogId":"1813145167239188480"}'

# 将JSON字符串解析为字典
data = json.loads(json_str)

# 将新的gold值转回为字符串，并更新字典
data['gold'] = str(gold_value)

# 如果需要将更新后的字典转回JSON字符串
new_json_str = json.dumps(data)

os.system('git add gold。json')
os.system('git commit -m "Update gold json"')
os.system('git push')
