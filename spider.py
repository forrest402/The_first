import re
import time
import requests
from My_Tools import get_headers
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_id():
    music_ids = []
    name = input("请输入你要爬取的歌曲或歌手:")
    url = "https://music.163.com/#/search/m/?s=%s" % name
    opt = webdriver.EdgeOptions()
    opt.headless = True
    driver = webdriver.Edge(options=opt)
    driver.get(url)
    driver.switch_to.frame("contentFrame")
    driver.find_element(by=By.CLASS_NAME, value="srchsongst")
    news = str(driver.page_source)
    data = re.compile('href="/song\Wid=(.*?)"').findall(news)
    for i in data:
        music_ids.append(i)
    driver.switch_to.default_content()
    driver.quit()
    return music_ids

def get_music(ids):
    url_base = "http://music.163.com/song/media/outer/url?id="
    cont = 0
    if os.path.exists("music") is False:
        os.mkdir("music")
    for i in ids:
        music_url = url_base + i + ".mp3"
        res = requests.get(music_url).content
        with open(r"music/%d.mp3"% cont, "wb")as f:
            f.write(res)
        cont += 1

if __name__ == "__main__":
    ids = get_id()
    get_music(ids)
