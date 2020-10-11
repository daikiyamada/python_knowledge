import numpy as np
import matplotlib.pylab as plt

"""
step_function
-----------
@param {array} np.array()　int型の配列をreturnする
"""
def step_function(x):
    return np.array(x > 0, dtype=np.int)

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
