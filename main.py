import requests
import re
import time
import os


# author ： AHUI@CCUT


def main():
    # n为剩余流量
    n = 15
    a = requests.get('http://222.28.211.100/')
    content = a.content
    text = content.decode('gb2312')
    info = re.findall('time=.*', text)
    info_c = info[0]
    info_c = info_c.replace("\r", '')
    info_c = info_c.replace("'", '')
    info_c = info_c.replace(" ", '')

    info_c_lis = info_c.split(";")
    # print(info_c_lis)
    target = 1024 * n * 1024
    tim = int(info_c_lis[0].replace("time=", ""))
    flow = int(info_c_lis[1].replace("flow=", ""))
    flow2 = round(flow/1024/1024,4)
    remain = int(target - flow)
    remain2 = round(remain/1024,2)
    os.system('cls')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(f"已用时间: {tim} 分钟")
    print(f"已用流量: {flow2} GB")
    print(f"剩余流量: {remain2} MB")
    # 此处为刷新间隔
    time.sleep(1)

if __name__ == '__main__':
    while True:
        main()
        