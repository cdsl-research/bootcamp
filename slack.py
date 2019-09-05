#import slackweb

#slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
#slack.notify(text="pythonからslackさんへ")

import requests
import json

requests.post('https://hooks.slack.com/services/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', data = json.dumps({
    'text': u'Hello,World!', # 投稿するテキスト
    'username': u'yoshiki', # 投稿のユーザー名
    'icon_emoji': u':ghost:', # 投稿のプロフィール画像に入れる絵文字
    'link_names': 1, # メンションを有効にする
}))