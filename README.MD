# YQExportMD
#
## 1、写在前面

![Version](https://img.shields.io/badge/Version-1.2.0-blue) ![License](https://img.shields.io/badge/license-MIT-yellow) ![python](https://img.shields.io/badge/python->=3.6-orange)

简介：ExportMD 语雀知识库自动导出为 Markdown 格式，支持同时导出多个知识库。但 ExportMD 导出连续三张图片时，会出现错误，只有第一张图片的内容会被识别，本复刻版本增加了正则表达式，修复这一情况。

如有有问题，你可以在本仓库中提交 issue，也欢迎到语雀评论区和我交流！  

- YQExportMD 语雀评论区：https://www.yuque.com/shenweiyan/wow/qbo2xht7s4gdcns3

- ExportMD-rectify-pics 语雀评论区：https://www.yuque.com/duzh929/blog/ocffqg

欢迎给我的语雀文档点赞，或者给我复刻的仓库 star！  

另外我想说明一下，复刻这个仓库的目的是为了防止重要的笔记丢失，让大家能够有一个本地的 markdown 笔记备份，但我并不希望语雀因此流失用户，语雀真的是一款非常优秀的笔记软件，我会一直支持下去的！


### 版本 v1.2
在原有程序基础上增加了一些其他的使用小程序，如导出语雀的单篇文档, 并根据需要转换成 Hugo 格式博文等，以满足个人使用需要，也为后续需要的用户提供参考。


### 版本 v1.1
实际使用的时候有遇到一些小问题，主要是接口限制等会导致有时候请求失败
这里使用 [@stone0090](https://github.com/stone0090/ExportMD-rectify-pics) 的解决方案。  

https://github.com/stone0090/ExportMD-rectify-pics/blob/bf2b79ef0afaffcad78253cafa1760f45359623e/ExportMD.py#L198 

修改为同步导出，且每次导出等待 100ms
本人技术水平有限，感谢 [@stone0090](https://github.com/stone0090/ExportMD-rectify-pics)!的修复。

### 版本 v1.0
API 导出连着的图片时，会出现很多 `<br />`，这时连续图片中只有第一张图片会被识别
```
![image.png](https://cdn.nlark.com/xxx1.png)<br />![image.png](https://cdn.nlark.com/xxx2.png)<br />![image.png](https://cdn.nlark.com/xxx3.png)

```
为了解决这一问题，在原来的 ExportMD 基础上，我增加了正则表达式，现在连续图片的导出已经没有问题
这里特别感谢 ExportMD！

## 2、安装

### 环境要求
 - python >= 3.6

### 安装 python 依赖

```bash
# 由于 PyInquirer-1.0.3 和 prompt-toolkit-1.0.14 会导致 ipython 出现异常，无法启动
# 因此 requirements.txt 降低了 PyInquirer 的版本至 1.0.0
pip3 install -r requirements.txt
```
---

## 3、使用

## 获取 namespace
知识库 namespace：知识库 URL 中路径部分

知识库 [https://www.yuque.com/YourYuqueUserName](https://www.yuque.com/YourYuqueUserName)  对应的 *namespace* 为 *YourYuqueUserName*

## 获取 token
![2022 11 22-10 50 01](https://user-images.githubusercontent.com/26101369/203209965-f664a352-a2ef-4a02-934b-588d3e657972.png)
![2022 11 22-10 55 10](https://user-images.githubusercontent.com/26101369/203209990-fd178ebc-8a8c-4c5d-9c26-f2f81fd414ed.png)


## 使用 python3 运行
```bash
python3 ExportMD.py
```
## 输入 namespace 和 token
**`⬆ ⬇`移动，`space`选择，`a`全选，`i`反选，`Enter`确认** 
![2022 11 22-11 18 33](https://user-images.githubusercontent.com/26101369/203213817-7d84fab2-e6a0-4bee-905d-9d59ccc1dc3a.png)
![2022 11 22-11 24 04](https://user-images.githubusercontent.com/26101369/203213842-e0e79258-d145-474a-88fb-c285f3e5da26.png)


