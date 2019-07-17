# coding: UTF-8
# インストールした discord.py を読み込む
import discord
import random
# 自分のBotのアクセストークンに置き換えてください
TOKEN = ''

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    cmd = message.content.split("\n")
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if cmd[0] == 'コマンド':
        await message.channel.send('朝ごはん\n----------------------------------\n')
        await message.channel.send('昼ごはん\n----------------------------------\n')
        await message.channel.send('晩ごはん\n----------------------------------\n')
        await message.channel.send('朝ごはん表示\n追加\n追加したい料理\n----------------------------------\n')
        await message.channel.send('昼ごはん表示\n追加\n追加したい料理\n----------------------------------\n')
        await message.channel.send('晩ごはん表示\n追加\n追加したい料理\n----------------------------------\n')

    l = ["卵かけご飯","ヨーグルト","焼き魚","ピザパン","ウインナー"]
    a = random.sample(l,3)
    if message.content == '朝ごはん':   
        b = message.author.name + "さんには" + str(a) + "がおすすめです！"
        await message.channel.send(b)
    if message.content in a:
        text = message.content
        point = message.author.name + "さんは朝ごはんに" + text + "を選んだんだね！！！！！！"
        await message.channel.send(point)
        
    if cmd[0] == '朝ごはん表示':
        await message.channel.send(l)
        if cmd[1] == '追加':
            l.append(cmd[2])
            await message.channel.send('追加しました')
            await message.channel.send(l)


    e = ["ラーメン","うどん","卵かけご飯","ピザ","カツ丼"]
    k = random.sample(e,3)
    if message.content == '昼ごはん':
        w = message.author.name + "さんには" + str(k) + "がおすすめです！"
        await message.channel.send(w)
    if message.content in k:
        temp = message.content
        q = message.author.name + "さんは昼ごはんに" + temp + "を選んだんだね！！！！！！"
        await message.channel.send(q)

    if cmd[0] == '昼ごはん表示':
        await message.channel.send(e)
        if cmd[1] == '追加':
            e.append(cmd[2])
            await message.channel.send('追加しました')
            await message.channel.send(e)
    
    s = ["肉じゃが","鯖の味噌煮","瓦そば","麻婆豆腐","とんかつ"]
    r = random.sample(s,3)
    if message.content == '晩ごはん':
        u = message.author.name + "さんには" + str(r) + "がおすすめです！"
        await message.channel.send(u)
    if message.content in r:
        anm = message.content
        y = message.author.name + "さんは晩ごはんに" + anm + "を選んだんだね！！！！！！"
        await message.channel.send(y)

    if cmd[0] == '晩ごはん表示':
        await message.channel.send(s)
        if cmd[1] == '追加':
            s.append(cmd[2])
            await message.channel.send('追加しました')
            await message.channel.send(s)

    
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)