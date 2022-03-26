import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
"""
c = 5  # 尺度系数yita
k = 1.5  # 形状系数beta
"""


def weib(x, c, k):
    """
威布尔分布函数
    @param x:
    @return:
    """
    return (k / c) * (x / c) ** (k - 1) * np.exp(-(x / c) ** k)


def weib_acc(x, c, k):
    """
    寿命可靠度函数
    """
    return np.exp(-(x / c) ** k)


def weibull_fig(c,k):
    """
做威布尔概率密度函数
    """
    x = np.arange(1, 2500.) / 100.
    plt.plot(x, weib(x,c,k))
    plt.show()


def weibull_acc_fig(c,k):
    """
    基于威布尔分布的寿命可靠度函数
    """
    x = np.arange(1, 2500.) / 100.
    plt.plot(x, weib_acc(x,c,k))
    plt.show()


if __name__ == '__main__':
    # weibull_fig()
    weibull_acc_fig(c=5,k=1.5)
