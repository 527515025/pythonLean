# -*- coding: utf-8 -*-
# 用 drop out 解决 Overfitting 问题
import 手写数字识别.input_data  
import tensorflow as tf
mnist = 手写数字识别.input_data.read_data_sets("手写数字识别/MNIST_data/", one_hot=True)  

# 添加神经层的函数def add_layer(),它有四个参数：输入值、输入的大小、输出的大小和激励函数，我们设定默认的激励函数是None。也就是线性函数
def add_layer(inputs, in_size, out_size,layer_name, activation_function=None):
    # 定义权重,尽量是一个随机变量
    # 因为在生成初始参数时，随机变量(normal distribution) 会比全部为0要好很多，所以我们这里的weights 是一个 in_size行, out_size列的随机变量矩阵。   
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    # 在机器学习中，biases的推荐值不为0，所以我们这里是在0向量的基础上又加了0.1。
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    # 定义Wx_plus_b, 即神经网络未激活的值(预测的值)。其中，tf.matmul()是矩阵的乘法。
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    #  用dropout来解决过拟合 问题
    Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob)
    # activation_function ——激励函数（激励函数是非线性方程）为None时(线性关系)，输出就是当前的预测值——Wx_plus_b，
    # 不为None时，就把Wx_plus_b传到activation_function()函数中得到输出。
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        # 返回输出
        outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name + '/outputs', outputs)
    return outputs

# 保留数据 keep_prob
keep_prob = tf.placeholder(tf.float32)
xs = tf.placeholder(tf.float32,[None, 784]) #图像输入向量  每个图片有784 （28 ＊28） 个像素点
ys = tf.placeholder(tf.float32, [None,10]) #每个例子有10 个输出

# prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)
l1 = add_layer(xs, 784, 50, 'l1', activation_function=tf.nn.tanh)
prediction = add_layer(l1, 50, 10,'l2' ,activation_function=tf.nn.softmax)
#loss函数（即最优化目标函数）选用交叉熵函数。交叉熵用来衡量预测值和真实值的相似程度，如果完全相同，它们的交叉熵等于零 ,所以loss 越小 学的好
#分类一般都是 softmax＋ cross_entropy
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
reduction_indices=[1]))
tf.summary.scalar('loss', cross_entropy)

#train方法（最优化算法）采用梯度下降法。  优化器 如何让机器学习提升它的准确率。 tf.train.GradientDescentOptimizer()中的值（学习的效率）通常都小于1
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.Session()

merged = tf.summary.merge_all() # tensorflow >= 0.12
train_writer = tf.summary.FileWriter("/Users/yangyibo/test/logs/train",sess.graph)
test_writer = tf.summary.FileWriter("/Users/yangyibo/test/logs/test",sess.graph)

# 初始化变量
init= tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
    #开始train，每次只取100张图片，免得数据太多训练太慢
    batch_xs, batch_ys = mnist.train.next_batch(50)
    # 丢弃百分之40 的数据
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
    if i % 50 == 0:
        train_result = sess.run(merged, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 1})
        test_result = sess.run(merged, feed_dict={xs: mnist.test.images, ys: mnist.test.labels, keep_prob: 1})
        train_writer.add_summary(train_result,i)
        test_writer.add_summary(test_result,i)
