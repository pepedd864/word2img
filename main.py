# 1. 读入图片，指定宽度 缩放图片 解析颜色信息 保存字符文本
from docx.oxml.ns import qn

from img import *

process_img('img.jpg', 108, 1.0, '示例图')

# 2. 创建img.docx 文件，设计边距为"窄", 使用word 打开，并使用模拟输入，输入所有的字符
from docx import Document
from docx.shared import Cm, Pt

# 2.1
file_name = 'img.docx'
document = Document()
# 2.2设置页边距为"窄"
sections = document.sections
for section in sections:
    section.left_margin = Cm(1.27)
    section.right_margin = Cm(1.27)
    section.top_margin = Cm(1.27)
    section.bottom_margin = Cm(1.27)
# 设置默认字体样式
default_style = document.styles['Normal']
default_font = default_style.font
default_font.bold = True
default_font.name = 'Microsoft JhengHei'
default_style.element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
default_font.size = Pt(5)
# 设置行间距 为默认固定值5磅
default_paragraph_format = default_style.paragraph_format
default_paragraph_format.line_spacing = Pt(5)  # 5 磅
# 设置段前段后间距
default_paragraph_format.space_before = Pt(0)  # 段前间距
default_paragraph_format.space_after = Pt(0)  # 段后间距
# document.save(file_name)
# # 2.3 使用word 打开
import os
import time

#
# os.system(f'start {file_name}')
# time.sleep(3)

# 写入word
print(f"写入{file_name}")
with open('texts.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        document.add_paragraph(line)
document.save(file_name)

# # 2.4 模拟输入
# from keyboard import *
# import pyautogui
#
# with open('texts.txt', 'r') as f:
#     for line in f:
#         # 此处的line是中文，无法模拟输入，故换成拼音输入
#         n = int(len(line) / 3)
#         for _ in range(n):
#             real_write('xdd ')
#         real_write('\n')
# time.sleep(2)
# pyautogui.hotkey('ctrl', 's')
# time.sleep(1)
# pyautogui.hotkey('alt', 'f4')

# 3. 处理颜色
from color import *

print("处理颜色中...")
file_name = 'img.docx'
process_color(file_name)
time.sleep(3)
print(f"输出到output_{file_name}中")
os.system(f'start output_{file_name}')
