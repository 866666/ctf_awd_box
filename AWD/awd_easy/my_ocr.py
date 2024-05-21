# coding:utf-8
# 从指定链接获取验证码并识别字符串
import requests
from bs4 import BeautifulSoup
import ddddocr


def get_code(url):
    ocr = ddddocr.DdddOcr()
    r = requests.get(url)
    img = r.content
    text = ocr.classification(img)
    return text


if __name__ == "__main__":
    url = "https://github.com/ypwhs/captcha_break"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    images = soup.find_all("img")
    for image in images:
        print(image.get("src"))
    print(images[0].get("src"))
    print(get_code(images[0].get("src")))
