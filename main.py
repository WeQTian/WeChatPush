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
    pushWeChatMsg = WeChatPush('wx896cf855276b73fd', '749d46813f3966e4a305f235ec60728a',
                               '8OuSnMT_EgVkbClLi-AFCpeJ5E31BUm0w1dudcgo3E0')
    # print(pushWeChatMsg.getWeChatToken())
    # print(pushWeChatMsg.getReceiveId())
    # print(WeChatPush.rainbowFart())
    print(pushWeChatMsg.pushWeChatMessage())
