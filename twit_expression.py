# coding:utf-8

import tweepy

#ここにAPIのKeyとか書き込む
Consumer_key = ''
Consumer_secret = ''
Access_token = ''
Access_secret = ''


auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

api = tweepy.API(auth)

print('ok')

#ここに自分のIDを
id = ""
#api.update_status(status="テスト\nテスト\n\n aaa")←呟けるぞ！

tweet = api.user_timeline(id, count=1)#最新1件のツイートの情報全てを取得

for i in tweet:#中を1つ1つ解析
    #print(i.text)
    tweetText = i.text#text(文章)だけをとって、代入

print(tweetText)

import re
patternHappy = re.findall("ありがとう|嬉しい|最高|好き|笑",tweetText)
patternSad = re.findall("辛い|つらい|悲しい|泣|疲れ", tweetText)
patternAngry = re.findall("クソ|最悪|死ね|ゴミ", tweetText)

#マッチした配列の数をカウントする
#print(patternAngry)
#print(len(patternAngry))

lenHap = len(patternHappy)
lenSad = len(patternSad)
lenAng = len(patternAngry)

if lenHap > lenSad and lenHap > lenAng:
    #笑顔に
    api.update_profile_image("happy.png")
    print("changed Happy")
elif lenSad > lenHap and lenSad > lenAng:
    #悲しく
    api.update_profile_image("sad.png")
    print("changed Sad")
elif lenAng > lenHap and lenAng > lenSad:
    #怒る
    api.update_profile_image("ang.png")
    print("changed Angry")
else:
    api.update_profile_image("default.jpg")
