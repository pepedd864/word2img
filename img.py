import colorsys
import json

from PIL import Image


def process_img(img: str, w: int, r: float, str: str):
    """
    读入图片，指定宽度 缩放图片 解析颜色信息 保存字符文本
    :param img: 图片路径
    :param w: 指定宽度
    :param r: 高宽比
    :param str: 保存字符文本
    :return:
    """
    # 1. 缩放图片
    image = Image.open(img)
    width, height = image.width, image.height
    resized_image = image.resize((w, int(height / width * w * r)))
    resized_image.save(f'resized_{img}')
    data = resized_image.load()
    # 2. 存储字符文本到文件中
    texts = ''
    for x in range(resized_image.height):
        text = str * int(resized_image.width / len(str)) + '\n'
        texts += text
    with open('texts.txt', 'w') as f:
        f.write(texts)
    # 3. 处理图片颜色信息
    print(f'缩放后的图片的宽高: {resized_image.width} {resized_image.height}')
    colors = []
    for j in range(resized_image.height):
        for i in range(resized_image.width):
            px = data[i, j]
            density = max(px)
            h, s, v = colorsys.rgb_to_hsv(*[d / 255 for d in px])
            # 因为字的背景是白色的，所以把颜色的饱和度提升了一点
            s *= 1.2
            s = min(s, 1)
            # 转为rgb,存入colors中
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            colors.append([int(r * 255), int(g * 255), int(b * 255)])
    # 4. 保存颜色信息
    with open('colors.json', 'w') as f:
        json.dump(colors, f)
