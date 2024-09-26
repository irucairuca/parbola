import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import japanize_matplotlib

# アニメを作る初期設定
fig = plt.figure()
ims = []
#重力加速度
g=9.8
#放物線面の広さ
x_0=np.linspace(-3,3,100)

#ボールを落とす座標
x_1=2
y_1=5
#初速度
v_x=0
v_y=0
#加速度
a_x=0
a_y=-g

#時間
t=0
#時間の刻み幅
delta_t=0.01
while(t<10):
  im=[]
  #ボールが放物面に衝突したら反射する。決して放物面の下に行ってはならない。
  if (x_1)**2>y_1:
    #放物線の接線ベクトル(1+2j*x_1)を基準平面として反射する。（完全弾性衝突とは、入射角と反射角が等しい反射と同じ現象である）
    theta=np.angle((v_x+1j*v_y)/(1+2j*x_1))
    v=(((-1-2j*x_1)/abs(-1-2j*x_1))/(np.cos(theta)+1j*np.sin(theta)))*(v_x+1j*v_y)
    #反射する方向は、必ずy軸側に向かうようにする。つまり放物線の内部でのみ反射を繰り返すものとする。
    if x_1>0:
      v_x=-v.real
      v_y=v.imag
    else:
      v_x=v.real
      v_y=v.imag
  #ボールの速度と位置の更新
  v_x=v_x+a_x*delta_t
  v_y=v_y+a_y*delta_t
  x_1=x_1+v_x*delta_t
  y_1=y_1+v_y*delta_t
  #放物面の描写
  im1=plt.plot(x_0,x_0**2)
  #ボールの描写
  im2=plt.plot(x_1,y_1,"o",color="red")
  ims.append(im1+im2)
  #時間の更新
  t=t+delta_t

# 複数枚のプロットを 20ms ごとに表示
ani = animation.ArtistAnimation(fig, ims, interval=20)
#保存
ani.save("放物線の焦点.gif", writer="pillow")
