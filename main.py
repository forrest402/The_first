import time
import random
import requests
from My_Tools import get_headers
from get_ensekey import get_params
import re
import pandas as pd
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from Stop_word import get_stop_dic
import jieba
from spider import get_id, get_music
from snownlp import SnowNLP as SNP

def get_comment(sing_id, page, url, header):
    arr = []
    for i in range(1, page+3):
        params, encseKey = get_params(i)
        data = {
            "params": params,
            "encSecKey": encseKey
        }
        res = requests.post(url, headers=get_headers(), params=data)
        time.sleep(random.randint(1, 5))
        res = str(res.json())
        content = re.compile("'content': '(.*?)'").findall(res)
        nick_names = re.compile("'nickname': '(.*?)'").findall(res)
        for k in range(len(content)):
            content[k] = clean_data(content[k])
            nick_names[k] = clean_data(nick_names[k])
            arr.append([nick_names[k], content[k]])
    return arr
def clean_data(data):
    data = re.sub(re.compile(" |\\n|\\r|\\t"), "", data)
    return data
def To_csv(my_data):
    d = pd.DataFrame(my_data, columns=["name", "comment"])
    d.to_csv("1.csv", encoding="utf_8_sig")


def get_world_clould(file_path):
    bg = plt.imread("bg.jpg")
    data = pd.read_csv(file_path)
    # print(data.head())
    strings = data["comment"]
    new_str = ""
    for i in strings.values:
        new_str += " ".join(jieba.cut(i))
    # print(new_str)
    my_word = WordCloud(
        font_path="./AdobeHeitiStd-Regular.ttf",
        stopwords=get_stop_dic(),
        max_words=200,
        background_color="white",
        width=800,
        height=600,
        min_word_length=4
    )
    my_word.generate_from_text(new_str)
    bg_color = ImageColorGenerator(bg)
    my_word.recolor(color_func=bg_color)
    plt.imshow(my_word, interpolation="bilinear")
    plt.axis("off")
    plt.close()
    # plt.show()
    my_word.to_file("word_cloud.jpg")
def get_qinggan(file_path):
    data = pd.read_csv(file_path)
    news = data["comment"].values
    arr = []
    my_data = []
    prv_cont = 0
    uprv_cont = 0
    for i in news:
        string = i
        s = SNP(u"%s" % string)
        content = s.sentiments
        if content > 0.5:
            prv_cont += 1
        else:
            uprv_cont += 1
        arr.append(content)
    for i in range(20):
        my_data.append(random.choice(arr))
    plt.plot(my_data)
    plt.xlabel("sentiment analysis")
    plt.ylabel("Sentiment Index")
    # plt.show()
    plt.savefig("plt.png")
    if prv_cont > uprv_cont:
        print("由上图可得,所有评论为积极的")
    else:
        print("由上图可得,所有评论为消极的")

def get_news(id):
    song_id = id
    page = int(input("请输入你要爬取的页数:"))
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(song_id) + '?csrf_token='
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"}
    data = get_comment(song_id, page, url, header)
    return data

if __name__ == "__main__":
    my_id = get_id()
    data = get_news(my_id[0])
    To_csv(data)
    get_world_clould("1.csv")
    get_qinggan("1.csv")
    get_music(my_id)

