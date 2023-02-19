import requests
import random
import json
import string
import time

url = 'http://ffwess.top/login.asp'
count = 1000000

server = json.loads(
    '{"servers":[{"name":"陆行鸟","part":["神意之地","幻影群岛","幻影群岛","萌芽池","红玉海","宇宙和音","沃仙曦染","晨曦王座"]},{"name":"莫古力","part":["潮风亭","神拳痕","白银乡","白金幻象","龙巢神殿","旅人栈桥","拂晓之间","梦羽宝境"]},{"name":"猫小胖","part":["海猫茶屋","柔风海湾","琥珀原","紫水栈桥","延夏","静语庄园","摩杜纳"]},{"name":"豆豆柴","part":["伊修加德","太阳海岸","银泪湖","水晶塔","红茶川"]}]}')


def RandomPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    randomPre = random.choice(prelist)
    Number = "".join(random.choice("0123456789") for i in range(8))
    phoneNum = randomPre + Number
    return phoneNum


def GenPassword(length):
    ascii_len = int(length / 3)
    chars = ''
    for i in range(ascii_len):
        chars = chars + str(random.choice(string.ascii_letters))
    for i in range(length - ascii_len):
        chars = chars + str(random.choice(string.digits))
    return chars


for i in range(0, count):
    i = server['servers'][random.randint(0, 3)]
    i_name = i['name']
    i_part = i['part'][random.randint(0, len(i['part']) - 1)]
    i_pass = GenPassword(random.randint(8, 17))
    i_phone = str(RandomPhone())
    print(i_name + ": " + i_part + " - " + i_phone + " : " + i_pass)
    datas = {
        'qq': i_phone,
        'action': 'save',
        'pass': i_pass,
        'al': i_name.encode('gbk'),
        'qu': i_part.encode('gbk'),
        'dj': str(random.randint(33, 90))
    }
    try:
        x = requests.post(url, data=datas)
        print(x)
    except:
        pass
    time.sleep(random.randint(1, 3))
