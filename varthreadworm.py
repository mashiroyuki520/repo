import requests
from lxml import etree
from queue import Queue
import threading
import os
import time
a = time.time()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
}


def download():
    while True:
        # 判断队t1线程是否存活
        if not t1.is_alive():
            print('已全部解析完毕！')
            # 判断队列是否为空
            if q.empty():
                print('全部下载完成！')
                break
        img, count, page = q.get()
        r = requests.get(img, headers=headers)
        pic = r.content

        # 创建目录用于下载
        path = '/home/mashiroyuki/图片/第{}页/'.format(page)
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as e:
            print(e)

        try:
            with open(path + '{}.jpg'.format(count), 'wb') as f:
                f.write(pic)
                print('{}.jpg-----下载成功'.format(count))
        except:
            print('下载失败！')


def get_img(img_url, page):
    r = requests.get(img_url, headers=headers)
    html = r.content.decode('gbk')
    tree = etree.HTML(html)
    # 图片链接
    img_list = tree.xpath('//div[@id="main"]/div[@class="slist"]/ul/li/a/img/@src')
    # print(img_list, len(img_list))
    count = 1
    for img in img_list:
        img = 'http://pic.netbian.com' + img
        # 下载图片
        # download(img, count)
        q.put([img, count, page])
        count = count + 1


def main():
    # 启始url
    url = 'http://pic.netbian.com/4kdongman/'
    req = requests.get(url, headers=headers)
    html = req.content.decode('gbk')
    # print(html)
    tree = etree.HTML(html)
    # 提取壁纸总页数
    num = tree.xpath('//div[@class="page"]/a[last() - 1]/text()')[0]
    for i in range(int(num)):

        img_url = url + 'index_{}.html'.format(i + 1)
        if i == 0:
            img_url = url
        # print(img_url)
        # 获取图片链接
        get_img(img_url, i + 1)


if __name__ == '__main__':
    # 创建队列
    q = Queue()
    lock = threading.Lock()

    # 创建线程
    t1 = threading.Thread(target=main)
    t2 = threading.Thread(target=download)
    t3 = threading.Thread(target=download)
    t4 = threading.Thread(target=download)
    t5 = threading.Thread(target=download)

    # 开启线程
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    b = time.time()
    print(b-a)



