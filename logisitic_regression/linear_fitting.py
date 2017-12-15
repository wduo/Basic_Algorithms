# http://blog.csdn.net/lizhe_dashuju/article/details/49887431

#!/usr/bin/env python 
#! -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
from numpy import *

#创建数据集
def load_dataset():
    n = 100
    X = [[1, 0.005*xi] for xi in range(1, 100)]
    Y = [2*xi[1]  for xi in X]
    return X, Y

#梯度下降法求解线性回归
def grad_descent(X, Y):
    X = mat(X)
    Y = mat(Y)
    row, col = shape(X)
    alpha = 0.001
    maxIter = 5000
    W = ones((1, col))
    for k in range(maxIter):
        W = W + alpha * (Y - W*X.transpose())*X
    return W

def main():
    X, Y = load_dataset()
    W = grad_descent(X, Y)
    print("W = ", W)

    #绘图
    x = [xi[1] for xi in X]
    y = Y
    plt.plot(x, y, marker="*")
    xM = mat(X)
    y2 = W*xM.transpose()
    y22 = [y2[0,i] for i in range(y2.shape[1]) ]
    plt.plot(x, y22, marker="o")
    plt.show()

if __name__ == "__main__":
    main()