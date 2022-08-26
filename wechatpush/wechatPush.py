# -*- coding:utf-8 _*_
"""
@Project    : WeChatPush 
@File       : wechatPush.py
@Author     : 晴天 
@Time       : 2022-08-26 16:15 
@Annotation : 微信推送消息
"""
import requests
import random


class WeChatPush:

    def __init__(self, appid, secret, template_id):
        """
        :param appid: 微信appID
        :param secret: 微信secret
        :param template_id: 微信模板ID
        """
        self.appid = appid
        self.secret = secret
        self.template_id = template_id

    def getWeChatToken(self):
        """
        获取微信Token
        :return: 返回微信Token
        """
        header = {
            'Content-Type': 'application/json;encoding=utf-8'
        }
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.appid}&secret" \
              f"={self.secret}"
        weChatToken = requests.get(url=url, headers=header).json()  # 发送请求到微信获取Token
        access_token = weChatToken['access_token']  # 提取微信Token
        # print(access_token)
        return access_token

    def getReceiveId(self):
        """
        获取要接收消息的用户ID
        :return: 返回用户ID
        """
        header = {
            'Content-Type': 'application/json;encoding=utf-8'
        }
        url = f"https://api.weixin.qq.com/cgi-bin/user/get?access_token={self.getWeChatToken()}&next_openid="
        receiveId = requests.get(url=url, headers=header).json()
        # print(receiveId['data']['openid'][0])
        return receiveId['data']['openid'][0]

    # 随机颜色
    @staticmethod
    def randomColor():
        return "#%06x" % random.randint(0, 0xFFFFFF)

    # 彩虹屁
    @staticmethod
    def rainbowFart():
        words = requests.get("https://api.shadiao.pro/chp")
        if words.status_code != 200:  # HTTP状态码不为200时重发一次请求
            return WeChatPush.rainbowFart()
        return words.json()['data']['text']

    def pushWeChatMessage(self):
        """
        发送推送消息
        :return: 返回成功/失败
        """
        header = {
            'Content-Type': 'application/json;encoding=utf-8'
        }
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={self.getWeChatToken()}"
        msgData = {
            "touser": f"{self.getReceiveId()}",
            "topcolor": "#FF0000",
            "url": "https://www.baidu.com",
            "template_id": f"{self.template_id}",
            "data": {
                "name": {
                    "value": "鹤熙",
                    "color": f"{self.randomColor()}"
                },
                "gender": {
                    "value": "女",
                    "color": f"{self.randomColor()}"
                },
                "age": {
                    "value": "26",
                    "color": f"{self.randomColor()}"
                },
                "hobby": {
                    "value": f"{self.rainbowFart()}",
                    "color": f"{self.randomColor()}"
                },
            }
        }
        pushMsg = requests.post(url=url, json=msgData, headers=header).json()
        # print(pushMsg)
        if pushMsg['errcode'] == 0:
            return '消息发送成功{}'.format(pushMsg['errmsg'])
        else:
            return '消息发送失败{}'.format(pushMsg['errmsg'])
