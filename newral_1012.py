import numpy as np
import matplotlib.pylab as plt

"""
step_function:ステップ関数

sigmoid：シグモイド関数
"""
def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def ReLU(x):
    return np.maximum(0,x)

"""
description
-----------
np.arrange(start,stop,step)：start→stopまでstepの間隔で配列を作成
"""
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y 軸の範囲を指定 plt.show()
plt.show()

y2=sigmoid(x)
plt.plot(x,y2)
plt.ylim(-0.1,1.1)
plt.show()

y = ReLU(x)
plt.plot(x,y)
plt.ylim(-0.1,5)
plt.show()
