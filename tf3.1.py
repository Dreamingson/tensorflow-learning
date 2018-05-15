import tensorflow as ts
a = ts.constant([1.0,2.0])
b = ts.constant([3.0,4.0])
result = a+b
print(result) # 张量 计算图


x = ts.constant([[1.0,2.0]])
w = ts.constant([[3.0],[4.0]])
y = ts.matmul(x,w)
print(y)


with ts.Session() as sess:# 会话
    print(sess.run(y))
