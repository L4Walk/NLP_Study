# coding:utf-8

import jieba
import collections


def read_text(file_path):
    # 1.打开文件
    with open(file_path, "r", encoding='utf-8') as f:  # 打开文件
        data = f.readlines()
        word_list = []
        # 2. 按行遍历文件
        for line in data:
            line = line.strip()
            words = jieba.cut(line)
            for word in words:
                word_list.append(word)
    # 3. 统计列表中每个字符出现的次数
    counter = collections.Counter(word_list).most_common()
    print(counter)


def main():
    file_path = "test.txt"
    read_text(file_path)

if __name__ == '__main__':
    main()