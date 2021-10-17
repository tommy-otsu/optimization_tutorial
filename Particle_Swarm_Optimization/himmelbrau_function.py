#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt


def f(x):
    """最小値を求めたい関数"""
    return x ** 2


def main():
    x = np.arange(-2, 2, 0.1)

    y = f(x)
    plt.plot(x, y, label='f(x)')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
