# -*- coding:utf-8 _*_
"""
@Project    : WeChatPush 
@File       : main.py 
@Author     : 晴天 
@Time       : 2022-08-26 16:13 
@Annotation : 程序启动入口
"""
from wechatpush.wechatPush import WeChatPush

if __name__ == '__main__':
    pushWeChatMsg = WeChatPush('微信APPID', '微信secret',
                               '模板消息ID')
    # print(pushWeChatMsg.getWeChatToken())
    # print(pushWeChatMsg.getReceiveId())
    # print(WeChatPush.rainbowFart())
    print(pushWeChatMsg.pushWeChatMessage())
