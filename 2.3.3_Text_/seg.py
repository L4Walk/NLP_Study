import jieba
import jieba.analyse
import codecs

# 将文本文件分词
def process_wiki_text(origin_file, target_file):
        with codecs.open(origin_file, 'r', 'utf-8') as inp, codecs.open(target_file, 'w', 'utf-8') as outp:
            line = inp.readline()
            line_num = 1
            while line:
                print('---处理', line_num, '文档----------')
                line_seg = " ".join(jieba.cut(line))
                # 写入目标文件
                outp.writelines(line_seg)
                line_num = line_num + 1
                line = inp.readline()
                if line_num == 101:
                    break

        # 关闭文件
        inp.close()
        outp.close()


def main():
    process_wiki_text('wiki.zh.txt', 'wiki.zh.txt.seg')


if __name__ == '__main__':
    main()

    