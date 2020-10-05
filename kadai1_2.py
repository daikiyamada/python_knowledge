#モジュールのインストール
import numpy as np
import matplotlib.pyplot as plt
import math

#linalg.norm()：ノルムを出力
def alpha(r):
    return -A*(r/np.linalg.norm(r))

r = np.array([1,0,0])
v = np.array([0,1,0])
G = 1.0
M = 1.0
#A = np.linalg.norm(v)**2/np.linalg.norm(r)
#A**B：AのB乗
A = -G*M*r/np.linalg.norm(r)**3
Tmax = 2*math.pi
T = np.linspace(0,Tmax,100)
h = T[1] - T[0]
X = []
Y = []
E = []

for t in T:
    r_0 = r
    r = r_0+v*h+h*h*alpha(r)/2.0
    v = v+(h/2.0)*(alpha(r)+alpha(r_0))
    X.append(r[0])
    Y.append(r[1])

#figure：描画領域の確保
plt.figure(1)
plt.plot(X,Y)
#gca：現在の描画オブジェクトを返す
#set_aspect：アスペクト比を整えるらしい（よくわからん）
plt.gca().set_aspect('equal',adjustable = 'box')
plt.show()
