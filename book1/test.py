print('\n'.join([''.join([('xiaoshanxue'[(x-y)%10]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))


from time import sleep
import requests
s = input("请主人输入话题：")
while True:
    resp = requests.post("http://www.tuling123.com/openapi/api",data={"key": "4fede3c4384846b9a7d0456a5e1e2943", "info": s, })
    resp = resp.json()
    sleep(1)
    print('小鱼：', resp['text'])
    s = resp['text']
    resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s})
    resp.encoding = 'utf8'
    resp = resp.json()
    sleep(1)
    print('菲菲：', resp['content'])
