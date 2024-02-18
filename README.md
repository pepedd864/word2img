## 使用Word显示图片

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/4c644f87bb2c57419d4cad0182db25a8.png)

**原理**

> 通过设置每个字的颜色从而拼成一整副画，字越小且单个字的面积越大，显示的效果就越清晰。

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/406eb1809ecbe7112e7f551d7738ed1c.png)

### 1. 使用

克隆项目到本地

进入项目文件夹，输入命令创建虚拟环境

```bash
python -m venv .venv
```

激活环境

```bash
.venv\Scripts\activate
```

安装依赖

```bash
pip install -r requirements.txt
```

项目目录结构

```
word2img
├── README.md               # 描述文件
├── color.py                # 处理颜色
├── colors.json             # 生成的图片颜色信息
├── img.docx                # 根据图片大小自适应的文字文档
├── img.jpg                 # 原图片，建议为竖屏文件
├── img.py                  # 处理图片
├── keyboard.py             # 模拟输入，根据需要开启
├── main.py                 # 主入口，包括读入图片，创建文档等等
├── output_img.docx         # 输出的文档
├── requirements.txt        # 项目依赖
├── resized_img.jpg         # 缩放后的图片
└── texts.txt               # 根据缩放后的图片生成的文字
```

使用本程序，你需要自行准备图片，你需要显示的字体，你需要显示的文字，和字体大小等等

这些都可以根据需要定制

![](https://picgo-img-repo.oss-cn-beijing.aliyuncs.com/img/aa3f5389bce350b4d322d6f179d92014.png)

运行项目

```bash
python main.py
```

便可得到结果



#### 2. 后续

可能研究如何在word中显示视频(已知word会占用文件，导致无法在打开word的状态下写入文件，后续看解决方案)