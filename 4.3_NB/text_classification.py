# coding=utf-8
import os
import jieba
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


# 分词d
def load_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
    titles = []  # 样本数据
    labels = []  # 标签
    for line in lines:
        line = line.encode('unicode-escape').decode('unicode-escape')
        line = line.strip().rstrip('\n')
        _lines = line.split('---')
        if len(_lines) != 2:
            continue
        label, title = _lines
        words = jieba.cut(title)
        s = ''
        for w in words:
            s += w + ' '
        s = s.strip()
        titles.append(s)
        labels.append(label)
    return titles, labels


# 加载数据
def load_data(_dir):
    file_list = os.listdir(_dir)

    titles_list = []
    labels_list = []

    for file_name in file_list:
        file_path = _dir + '/' + file_name
        titles, labels = load_file(file_path)
        titles_list += titles
        labels_list += labels

    return titles_list, labels_list


# 加载停用词
def load_stopwords(file_path):
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
        words = []

    for line in lines:
        line = line.encode('unicode-escape').decode('unicode-escape')
        line = line.strip('\n')
        words.append(line)
    return words


def main():
    stop_words = load_stopwords('stop_word/stopword.txt')
    # 加载训练数据
    train_datas, train_labels = load_data('train_data')
    # 文本向量表示
    tf = CountVectorizer(stop_words=stop_words, max_df=0.5)
    train_features = tf.fit_transform(train_datas)
    train_features_arr = train_features.toarray()
    # 多项式贝叶斯分类器
    clf = MultinomialNB(alpha=0.001).fit(train_features_arr, train_labels)
    test_datas, test_labels = load_data('test_data')
    test_features = tf.transform(test_datas)

    # 预测数据
    predicted_labels = clf.predict(test_features)
    # 计算准确率
    score = metrics.accuracy_score(test_labels, predicted_labels)
    print(score)

    joblib.dump(clf, 'nb.pkl')
    joblib.dump(tf, 'tf.pkl')


if __name__ == '__main__':
    main()
