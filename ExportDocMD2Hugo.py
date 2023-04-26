# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

######################################################################
__author__  = 'shumlab@foxmail.com'
__create__  = '2022-12-07'
__file__    = 'ExportDocMD2Hugo.py'
__license__ = '2022 All rights reserved.'
__doc__     = '导出语雀的单篇文档, 并根据需要转换成 Hugo 格式博文, 及通过镜像回源的方式处理对应的图片.'
#####################################################################
import requests, optparse, re
from bs4 import BeautifulSoup

def __main__():
    usage = "usage: python3 %prog [options] \n\nExample:\n"
    usage = usage + "    python3 %prog -u https://www.yuque.com/shenweiyan/cookbook/try-yuque-api -t '语雀;Python' -s cos.shenlab.cn -o"
    usage = usage + "\n\nDescription:\n"
    usage = usage + "    1. 导出语雀的单篇文档, 并根据需要转换成 Hugo 格式博文, 及通过镜像回源的方式处理对应的图片。\n"
    usage = usage + "    2. -u 不能为空。\n"
    usage = usage + "    3. -o 自动保存为 create_at-slug.md 格式的文件, 如 2022-12-08-try-yuque-api.md 。"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-u", "--url", dest="url", help="文章的 URL 访问地址")
    parser.add_option("-s", "--site", dest="site", default="cos.shenlab.cn", help="镜像回源的 URL 地址 (默认: cos.shenlab.cn)")
    parser.add_option("-t", "--tag", dest="tag", default="", help="文章的 TAG 标签, 多个标签用分号分隔 (默认: '')")
    parser.add_option("-o", "--out", dest="out", action="store_true", default=False, help="保存为 md 文档 (默认: create_at-slug.md) ")

    opts, args = parser.parse_args()
    if not opts.url:
        parser.error('提示：URL 不能为空！')

    url  = opts.url.strip()
    site = opts.site.strip()
    tag  = opts.tag.strip()
    out  = opts.out

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    resp = requests.request("GET", url, headers=headers)
    html = resp.text
    bs   = BeautifulSoup(html,"lxml")

    slug      = url.strip().split("/")[-2] if url.endswith("/") else url.strip().split("/")[-1]
    title     = bs.title.string.strip(' · 语雀$')
    create_at = bs.find("meta", {"name":"weibo:article:create_at"}).attrs['content']
    update_at = bs.find("meta", {"name":"weibo:article:update_at"}).attrs['content']
    create    = create_at.split()[0]
    update    = update_at.split()[0]
    outfile   = create_at.split()[0] + "-" + slug + ".md"
    tags_list = []
    for t in tag.strip().split(";"):
        t = t.strip()
        if t:
            tags_list.append(t)
    tags = '[\"%s\"]' % ('\",\"'.join(tags_list))

    post_meata = "---\ntitle: '%s'\nslug: '%s'\ndate: '%s'\nlastmod: '%s'\ntype: posts\npublished: true\nauthor: 沈维燕\ntags: %s\n---\n\n" % (title, slug, create, update, tags)
    post_meata = post_meata + "> 📢本 文章同步自作者的[语雀知识库](https://www.yuque.com/shenweiyan/)，请点击[这里](%s)阅读原文。\n\n" % url

    md_url = url.strip("/")+'/markdown?plain=true&linebreak=false&anchor=false'
    md_res = requests.request("GET", md_url, headers=headers)
    body   = md_res.text
    #body = re.sub("<a name=\".*\"></a>","", body)  # 正则去除语雀导出的<a>标签
    #body = re.sub("\x00", "", body) # 去除不可见字符\x00
    #body = re.sub("\x05", "", body) # 去除不可见字符\x05
    body = re.sub(r'\<br \/\>!\[image.png\]',"\n![image.png]",body) # 正则去除语雀导出的图片后紧跟的<br \>标签
    body = re.sub(r'\)\<br \/\>', ")\n", body)  # 正则去除语雀导出的图片后紧跟的<br \>标签
    #pattern = r"!\[(?P<img_name>.*?)\]" \
    #          r"\((?P<img_src>https:\/\/cdn\.nlark\.com\/(?P<img_pre>yuque.*\/(?P<slug>\d+))\/(?P<filename>.*?\.[a-zA-z]+)).*\)"
    pattern  = r"!\[(?P<img_name>.*?)\]" \
               r"\((?P<yuque_imgurl>(?P<cdn_lark>https://cdn\.nlark\.com)/(?P<img_pre>yuque/[0-9]*/\d+/[\w]*/\d+)/(?P<filename>[\w-]*\.[a-zA-Z]*))[^!]*\)"
    repl     = r"![\g<img_name>](https://%s/\g<img_pre>/\g<filename>)" % site
    new_body = re.sub(pattern, repl, body)

    if out:
        with open(outfile, "w") as md:
            md.write(post_meata+new_body)
        print("√ 结果已保存为: %s\n√ 结果保存成功！" % outfile)
    else:
        print(post_meata)
        print(new_body)


if __name__ == "__main__":
    __main__()
