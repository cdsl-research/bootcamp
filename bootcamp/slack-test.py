#import slackweb

#slack = slackweb.Slack(url="webhookで取得したURL")
#slack.notify(text="pythonからslackさんへ")

import requests
import json

requests.post('webhookで取得したURL', data = json.dumps({
    'text': u'Hello,World!', # 投稿するテキスト
    'username': u'yoshiki', # 投稿のユーザー名
    'icon_emoji': u':ghost:', # 投稿のプロフィール画像に入れる絵文字
    'link_names': 1, # メンションを有効にする
}))
