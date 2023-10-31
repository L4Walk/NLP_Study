import gensim
model = gensim.models.Word2Vec.load("wiki.zh.text.model")

# 查看前5个单词的词向量
count = 0
for word in model.wv.index2word:
    print(word, model.wv[word])
    count += 1

    if count == 5:
        break

# 查看“语言学”最接近的10个单词
result = model.wv.most_similar(u"语言学")
for e in result:
    print(e)

