import logging
import os.path
import sys
from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    # 获取日志信息
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: '
                               '%(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    # 打印日志
    logger.info("running %s" % ' '.join(sys.argv))
    # check and process input arguments
    if len(sys.argv) < 3:
        print(globals()['__doc__'] % locals())
        sys.exit(1)

    inp, outp = sys.argv[1:3]
    # inp:输入的数据集
    # outp:从压缩文件中获得的文本文件
    space = " "
    i = 0
    output = open(outp, 'w', encoding='utf-8')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(space.join(text) + "\n")
        i = i + 1
        if i % 200 == 0:
            logger.info("Saved " + str(i) + " articles")
            break

    output.close()  # 关闭文件
    logger.info("Finished Saved " + str(i) + "articles")