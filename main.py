# インストールした discord.py を読み込む
import discord
import random
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'J6nrgxAIX9Opb5_LVZQpx5g7Tl0tiyy8'

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
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '朝ごはん':
        m = "おはようございます" + message.author.name + "さん!"
        l = ["卵かけご飯","ヨーグルト","焼き魚","ピザパン","ウインナー"]
        n = random.sample(l,3)
        await message.channel.send(n)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)