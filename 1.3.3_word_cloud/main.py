#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词  
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('./resource/stopword.txt')  # 这里加载停用词的路径  
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


inputs = open('./data/lightning.txt', 'r', encoding='gbk')
outputs = open('output.txt', 'w', encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)  # 返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()


mask_img = np.array(Image.open("resource/test.png"))  # 打开背景图片
inputs = open('output.txt', 'r', encoding='utf-8')    # 分词结果
mytext = inputs.read()
wordcloud = WordCloud(background_color="white", max_words=500, width=2000, height=1600, margin=2,
                      font_path="resource/simsun.ttf", mask=mask_img).generate(mytext)
plt.imshow(wordcloud)   # 构建词云
plt.show()
plt.savefig("result.png") # 保存词云图片
plt.axis("off")

