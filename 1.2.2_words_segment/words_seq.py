# encoding=utf-8
import jieba

#jieba.enable_paddle()  # 启动paddle模式


def word_segment():
    #strs = "我来到北京清华大学"
    strs = "我来到杭州中国计量大学"
    seg_list = jieba.cut(strs, cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式
    seg_list = jieba.cut(strs, cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
 #   seg_list = jieba.cut(strs, use_paddle=True)
 #   print("Paddele mode: " + "/ ".join(seg_list))  # paddle模式
    seg_list = jieba.cut_for_search(strs)
    print("Search mode: " + "/ ".join(seg_list))  # 搜索引擎模式


def main():
    word_segment()


if __name__ == '__main__':
    main()
