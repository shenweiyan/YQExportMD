# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

######################################################################
__author__  = 'weiyanshum@foxmail.com'
__create__  = '2023-05-08'
__file__    = 'match4debug.py'
__license__ = '2023 All rights reserved.'
__doc__     = 'The test script.'
#####################################################################
import re

site = "https://example.com"

body = '''
使用`yum install squashfs-tools`安装了`unsquashfs`并添加到 $PATH 中问题依然没法解决！！！![16f4cadef5c03cdafaae5847f3e0672.png](https://cdn.nlark.com/yuque/0/2023/png/126032/1682492426106-caac87ee-9aaa-466a-bf85-bb5f7d57d718.png#averageHue=%23110f0e&clientId=ua80697a5-cdd3-4&from=paste&height=1011&id=u36ebccac&originHeight=1011&originWidth=1377&originalType=binary&ratio=1&rotation=0&showTitle=false&size=114536&status=done&style=none&taskId=u91ceda16-2e9e-4101-9bbd-1231c77e8e2&title=&width=1377)初步测试 singularity build 也能正常使用了。
![](https://cdn.nlark.com/yuque/0/2023/png/126032/1681969636953-0ad0be8d-da7d-4e32-988b-ae0b9a01b646.png#averageHue=%230f0e0d&clientId=ua507dde2-8a4e-4&from=paste&height=1009&id=u7581be13&originHeight=1009&originWidth=1408&originalType=binary&ratio=1&rotation=0&showTitle=false&size=141513&status=done&style=none&taskId=u79267165-09df-496f-a3ba-4a417ee514d&title=&width=1408)
'''

pattern  = r"!\[(?P<img_name>.*?)\]" \
           r"\((?P<yuque_imgurl>(?P<cdn_lark>https:\/\/cdn\.nlark\.com)\/(?P<img_pre>yuque\/[0-9]\/\d+\/[\w]*\/\d+)\/(?P<filename>.*\.[a-zA-Z]+)).*\)"
repl     = r"![\g<img_name>](https://%s/\g<img_pre>/\g<filename>)" % site
new_body = re.sub(pattern, repl, body)

print(new_body)

if new_body == body:
    print("执行图片第二次匹配 ...")

pattern2 = r"!\[(?P<img_name>.*?)\]" \
           r"\((?P<img_src>https:\/\/cdn\.nlark\.com\/(?P<img_pre>yuque.*\/(?P<slug>\d+))\/(?P<filename>.*?\.[a-zA-z]+)).*\)"
repl2    = r"![\g<img_name>](https://%s/\g<img_pre>/\g<filename>)" % site
new_body = re.sub(pattern2, repl2, new_body)

