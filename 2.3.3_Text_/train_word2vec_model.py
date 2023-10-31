import logging
import os.path
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    if len(sys.argv) < 4:
        print(globals()['__doc__'] % locals())
        sys.exit(1)

    # inp:分好词的文本    outp1:训练好的模型    outp2:得到的词向量
    inp, outp1, outp2 = sys.argv[1:4]

    # 调用Word2vec模型训练词向量
    model = Word2Vec(LineSentence(inp), size=100, window=5, min_count=5, ● workers = multiprocessing.cpu_count())

    # 保存模型
    model.save(outp1)

    # 保存模型权重
    model.wv.save_word2vec_format(outp2, binary=False)