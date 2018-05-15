import tensorflow as tf
# 神经元线上的权重
w = tf.Variable(tf.random_normal([2,3],stddev=2,mean=0,seed=1)) # normal正态分布 [2,3]产生2*3的矩阵 stddev标准差 mean平均值 seed随机种子(去掉数目会不同)
tf.truncated_normal() # 去掉过大偏离点的正态分布
tf.random.uniform() # 平均分布
# tf.zeros([3,2],int32) # 全0数组
# tf.ones([3,2],int32) # 全1数组
# tf.fill([3,2],6) # 全定值数组
# tf.constant([3,2,1]) # 直接给值