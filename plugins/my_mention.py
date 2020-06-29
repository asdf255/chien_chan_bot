from slackbot.bot import respond_to  # @botname: で反応するデコーダ
from slackbot.bot import listen_to  # チャネル内発言で反応するデコーダ
from slacker import Slacker
import pandas as pd
import json
import requests
from time import sleep



slack = Slacker('')
Token = ""


username = "chien_chan"
icon_emoji = ":pien:"

userid = ""

target = ['つくばエクスプレス', 'ゆりかもめ','東京臨海高速鉄道りんかい線','新京成電鉄線','京王動物園線', '京王線',
          '京成千原線',
          '京成千葉線', '京成成田スカイアクセス線', '京成押上線', '京成本線', '京成金町線', '京王井の頭線',  '小田急多摩線', '小田急小田原線',
          '小田急江ノ島線',
           '日暮里・舎人ライナー', '東京メトロ丸ノ内線', '東京メトロ副都心線', '東京メトロ千代田線', '東京メトロ半蔵門線', '東京メトロ南北線', '東京メトロ日比谷線',
          '東京メトロ有楽町線',
          '東京メトロ東西線', '東京メトロ銀座線', '都営三田線', '都営大江戸線','都営新宿線','都営浅草線','東急多摩川線', '東急大井町線', '東急東横線', '東急池上線', '東急田園都市線', '東急目黒線', '東武亀戸線', '東武伊勢崎線',
          '東武佐野線',
          '東武日光線', '東武越生線', '東武アーバンパークライン', '東武スカイツリーライン', '横浜市営地下鉄グリーンライン', '横浜市営地下鉄ブルーライン', '秩父鉄道', '西武国分寺線',
          '西武多摩川線',
          '西武多摩湖線', '西武拝島線', '西武新宿線', '西武有楽町線', '西武池袋線', '西武狭山線', '西武秩父線', '西武西武園線', '西武豊島線',
          'JR成田エクスプレス',  'JR御殿場線',
          'JR上野東京ライン',  'JR中央本線', 'JR中央線', 'JR京浜東北', 'JR京葉線',  'JR南武線', 'JR埼京線', 'JR宇都宮線', 'JR山手線','JR成田線','JR根岸線', 'JR横浜線', 'JR横須賀線', 'JR武蔵野線', 'JR湘南新宿ライン','JR総武線快速', 'JR青梅線', 'JR高崎線', 'JR鶴見線',
          'JR烏山線', 'JR相模線', 'JR総武本線', 'JR総武線', 'JR鹿島線','JR小海線','JR川越線', 'JR常磐線','JR日光線', 'JR東北本線', 'JR東海道本線', 'JR東金線', 'JR水戸線', 'JR水郡線','JR両毛線', 'JR上越線', 'JR五日市線','JR吾妻線' , 'JR外房線','JR内房線','JR八高線',"銚子電鉄線"]

@listen_to('出')
def func(message):
    # message.send(":pien:"+"お気をつけて"+":pien:")
    message.react("one")
    print(message.body)
    id = message.body['user']
    df = pd.read_csv("sample.csv", encoding="utf-8", index_col=0)
    df = df.fillna("NULL")

    if sum(df["ID"] == id) == 1 :
        for index,row in df.iterrows():
            if row["ID"] == message.body['user']:
                if df['railA'][index]=='NULL':

                    attachments = [{
                        "color": "good",
                        "fields": [
                            {

                                "title": "使用路線は何ですか?",
                                "value": "`追加 路線A 路線B(任意) 路線C(任意)`\n"
                                "`(例) 追加 山手線 つくば`\n\n",
                                "short": "true",
                            }
                        ]
                    }]
                    post_payload(attachments, message)

                    break
        train_delay(message, df)
    else:
        attachments = [{
            "color": "good",
            "fields": [
                {

                    "title": "使用路線は何ですか?",
                    "value": "`追加 路線A 路線B(任意) 路線C(任意)`\n"
                             "`(例) 追加 山手線 つくば`\n\n",
                    "short": "true",
                }
            ]
        }]

        post_payload(attachments, message)
    df.to_csv("sample.csv", encoding="utf-8")
    exit()

@respond_to('出')
def func(message):
    print(message.body)
    id = message.body['user']
    df = pd.read_csv("sample.csv", encoding="utf-8", index_col=0)
    df = df.fillna("NULL")

    if sum(df["ID"] == id) == 1 :
        for index,row in df.iterrows():
            if row["ID"] == message.body['user']:
                if df['railA'][index]=='NULL':

                    attachments = [{
                        "color": "good",
                        "fields": [
                            {

                                "title": "使用路線は何ですか?",
                                "value": "`追加 路線A 路線B(任意) 路線C(任意)`\n"
                                "`(例) 追加 山手線 つくば`\n\n",
                                "short": "true",
                            }
                        ]
                    }]
                    post_payload(attachments, message)
                    break
        train_delay(message, df)
    else:
        attachments = [{
            "color": "good",
            "fields": [
                {

                    "title": "使用路線は何ですか?",
                    "value": "`追加 路線A 路線B(任意) 路線C(任意)`\n"
                             "`(例) 追加 山手線 つくば`\n\n",
                    "short": "true",
                }
            ]
        }]
        post_payload(attachments, message)
    df.to_csv("sample.csv", encoding="utf-8")
    exit()


@respond_to("追加")
def targets(message):
    df = pd.read_csv("sample.csv", encoding="utf-8", index_col=0)
    adds(message,df)
    exit()

def adds(message,df):
    text=message.body['text']
    add=text.replace("*"," ")
    add = add.split()
    print(message.body['text'])
    if len(add) == 1:
        error_attachments(message, "Error", "路線がないです。")
    try:
        if add[2] == '追加' and len([s for s in target if add[1] in s]) == 1 :
            t = add[2]
            add[2] = add[1]
            add[1] = t
            del add[0]
    except :
        pass

    for i in range(1,len(add)):
        l_in = [s for s in target if add[i] in s]
        print(l_in)
        if len(l_in) >= 2:
            error_attachments(message,"Error","複数検出されました。")
            error_attachments(message,"",str(l_in))
            error_attachments(message,"","再度入力してください。")

        elif len(add)>4:
            error_attachments(message,"Error","3つまで入力してください。")
            break
        elif len(l_in) == 1:
            df = ID_check(message, df,l_in[0])
            df.to_csv("sample.csv", encoding="utf-8")

        elif len(l_in) == 0:
            error_attachments(message,"Error",str(add[i])+"は対応していません。\n対応する路線<https://www.jreast.co.jp/press/2015/20151109.pdf|一覧>")


def ID_check(message,df,add_rail):
    df = df.fillna("NULL")
    for index,row in df.iterrows():
        if row['ID'] == message.body['user']:
            for columns_name,item in df.iteritems():
                if df.at[index,columns_name] == add_rail:
                    error_attachments(message, "Warning", "被りがあります。")
                    return df
                elif df.at[index,'railC'] != 'NULL':
                    error_attachments(message,"Error","登録できる路線は三つまでです。")
                    error_attachments(message,"",str(add_rail)+'追加できません。')
                    return df
                elif item[index] == 'NULL':
                    df.at[index,columns_name] = add_rail
                    add_attachments(add_rail,message)
                    return df
    df = df.append({'ID': message.body['user'], 'railA': add_rail}, ignore_index=True)
    add_attachments(add_rail, message)
    return df


def error_attachments(message,title,value):

    attachments = [{
        "color": "danger",
        "fields": [
            {

                "title": title,
                "value": value,
            }]
    }]
    post_payload(attachments, message)

def train_delay(message, df):

    rea = ""
    df_train =""
    df_train_yahoo = yahoo_delay()

    id = message.body['user']
    user = [[n,i] for n, i in enumerate(list(df["ID"])) if i == id]  # IDの番号がわかった
    use_index = user[0][0]
    if len(df[df["ID"] == id].index) >= 1:
        for columns_name , item in df.iteritems():
            if (columns_name == 'railA' or columns_name == 'railB' or columns_name == 'railC') and item[use_index] != 'NULL':

                try :
                    if len(df_train_yahoo):
                        if item[use_index] in df_train_yahoo:
                            go_work(message,str(item[use_index]),1)
                            break
                    for i in range(len(df_train["name"])+1):
                        if df_train.at[i,"name"] in item[use_index]:
                            go_work(message,str(item[use_index]),1)
                            break
                except :
                    go_work(message,str(item[use_index]),0)
                print(message)
            elif item[use_index] == 'NULL':
                break


def yahoo_delay():
    import requests
    from bs4 import BeautifulSoup

    delay = ""

    kanto_delay = requests.get(delay)

    kanto_soup = BeautifulSoup(kanto_delay.text, 'html.parser')

    aa = kanto_soup.find('div', class_="elmTblLstLine trouble")

    html_text = aa.text
    html_list = html_text.split()

    print(html_list)

    train = []
    for i in html_list:
        if i in target:
            train.append((i))
    print(train)
    return train



@respond_to("確認")
def df_look(message):
    message.react("parrot")
    df = pd.read_csv("sample.csv", encoding="utf-8", index_col=0)
    df = df.fillna("NULL")
    for index,row in df.iterrows():
        if row['ID'] == message.body['user']:
            a = ['railA','railB','railC']
            for i in a:
                if df[i][index] != "NULL":
                    rail_pic = picture_word(df[i][index])

                    message.send("*{0} {1}*".format(str(rail_pic),str(df[i][index])))

            break
    exit()
@respond_to("上書き")
def rewrite(message):
    df = pd.read_csv("sample.csv", encoding="utf-8", index_col=0)
    for index,row in df.iterrows():
        if row['ID'] == message.body['user']:
            df['railA'][index] = 'NULL'
            df['railB'][index] = 'NULL'
            df['railC'][index] = 'NULL'
            break
    adds(message,df)
    exit()


@respond_to("help")
def help_attachment(message):
    attachments = [{
        "color": "#ff0000",
        "fields": [
            {

                "title": "路線の追加",
                "value": "`追加 路線A 路線B(任意) 路線C(任意)`\n"
                         "(例) 追加 山手線 つくば\n\n"
                         "または\n"
                         "`絵文字A 路線A 追加`"
            }]
    }, {
        "color": "#ff00ff",
        "fields": [{
            "title": "路線の上書き",
            "value": "`上書き 路線A 路線B(任意) 路線C(任意)`\n"
                     "(例) 上書き 山手線 つくば\n\n",
        }]
    }, {
        "color":"#daa520",
        "fields": [{
            "title": "登録済みの絵文字と対応路線を確認",
            "value": "`一覧`"
        }]
    },
       {
        "color":"#008000",
        "fields": [{
            "title": "ユーザーの路線確認",
            "value": "`確認`"
        }]
    } ,{
            "color": "#00008b",
            "fields":
                [{
                    "value": "*取り扱い路線* \n<https://www.jreast.co.jp/press/2015/20151109.pdf|サイトに飛ぶ> ",

                }]
        }
    ]
    post_payload(attachments,message)
    exit()

def go_work(message,rail,num):
    t = ["OK","DELAY"]
    v = ["ちえんない","ちえんちえん"]
    c = ["good","danger"]
    rail_pic = picture_word(rail)
    attachments = [{
        "color": c[num],
        "fields": [
            {
                "title":"{0} {1} is {2}".format(rail_pic, rail,t[num]),

                #"title": +str(rail)+" IS "+str(t[num]),
                "value": v[num],
                "short": "true"
            }
        ]
    }]
    message.send("*{0} {1} is {2}*".format(rail_pic, rail,v[num]))



def add_attachments(add_rail,message):
    rail_pic = picture_word(add_rail)
    # attachments = [{
    #     "color": "good",
    #     "fields": [
    #         {
    #
    #             "title": str(rail_pic)+" "+str(add_rail),
    #             "value": str(add_rail)+"を追加しました。",
    #             "short": "false"
    #         }
    #     ]
    # }]

    me(str(rail_pic)+" *"+str(add_rail)+"を追加しました。*",message)

def me(a,message):
    message.send(a)

def first_attachments(add_rail,message):
    rail_pic = picture_word(add_rail)
    attachments = [{
        "color": "good",
        "fields": [
            {

                "title": str(rail_pic)+" "+str(add_rail),
                "value": str(add_rail)+"を追加しました。",
                "short": "false"
            }
        ]
    }]
    post_payload(attachments,message)

def first_not_attachments(add_rail,message):
    rail_pic = picture_word(add_rail)
    message.send(str(rail_pic) + " " + str(add_rail))
    message.send(str(add_rail) + "を追加しました。")



def post_payload(attachments,message):
    post_url = 'https://slack.com/api/chat.postMessage'
    channel = message.body["channel"]        #チャンネルのURLの末尾についている文字列

    payload = {
        'token': Token,
        'channel': channel,
        # 'username': username,
        # 'icon_emoji': icon_emoji,
        'as_user':'true',
        'attachments': json.dumps(attachments),
    #    'text': ':one:'
    }
    res = requests.post(post_url, data=payload)
    print(type(res),res)

def pic_chaker(rail_name):
    from pykakasi import kakasi
    kakasis = kakasi()  # Generate kakasi instance
    kakasis.setMode("J", "a")
    kakasis.setMode("H", "a")  # Hiragana to ascii
    kakasis.setMode("K", "a")  # Katakana to ascii
    kakasis.setMode("r", "Hepburn")
    conv = kakasis.getConverter()
    result = conv.do(rail_name)
    return (":train-"+str(result)+":")


@respond_to("一覧")
def all_view(message):
    for n, i in enumerate(target):
        message.send(picture_word(i) +" "+str(i) )
        sleep(0.4)
    exit()

def picture_word(rail_name):
    jr = ["JR小海線","JR上越線", "JR両毛線", "JR五日市線", "JR八高線", "JR内房線", "JR吾妻線", "JR外房線", "JR川越線", "JR常磐線", "JR日光線", "JR東北本線",
          "JR東海道本線", "JR東金線", "JR水戸線", "JR水郡線", "JR烏山線", "JR相模線", "JR総武本線", "JR総武線","JR鹿島線","JR小海線"]
    if rail_name in jr:
        return ":jr:"
    elif "日暮里・舎人ライナー" == rail_name:
        return ":train-nipporishaninrainaa:"
    else:
        return pic_chaker(rail_name)

@respond_to("退")
def go_home(message):
    id = message.body['user']
    df = pd.read_csv("sample.csv", encoding="utf-8", index_col=0)
    df = df.fillna("NULL")

    if sum(df["ID"] == id) == 1:
        for index, row in df.iterrows():
            if row["ID"] == message.body['user']:
                if df['railA'][index] == 'NULL':

                    attachments = [{
                        "color": "good",
                        "fields": [
                            {

                                "title": "使用路線は何ですか?",
                                "value": "`追加 路線A 路線B(任意) 路線C(任意)`\n"
                                         "`(例) 追加 山手線 つくば`\n\n",
                                "short": "true",
                            }
                        ]
                    }]
                    post_payload(attachments, message)

                    break
        train_delay(message, df)
    else:
        attachments = [{
            "color": "good",
            "fields": [
                {

                    "title": "使用路線は何ですか?",
                    "value": "`追加 路線A 路線B(任意) 路線C(任意)`\n"
                             "`(例) 追加 山手線 つくば`\n\n",
                    "short": "true",
                }
            ]
        }]
        post_payload(attachments, message)
    df.to_csv("sample.csv", encoding="utf-8")
    exit()
