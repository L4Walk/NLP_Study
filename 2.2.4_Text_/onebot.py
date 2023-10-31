from sklearn import preprocessing   # 导入预处理器模型

enc = preprocessing.OneHotEncoder()  # 调用独热编码
enc.fit([
    [0, 0, 3],
    [1, 1, 0],
    [0, 2, 1],
    [1, 0, 2]
])  # 训练集

res = enc.transform([[0, 1, 3]]).toarray()  # 将结果转换为数组
print(res)
