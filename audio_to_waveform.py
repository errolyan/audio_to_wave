#欢迎关注交流

import wave
import numpy as np
import matplotlib.pyplot as plt

filepath = "DataSet/yuexijiang.wav"
fwav = wave.open(filepath,)
print(fwav)

params = fwav.getparams()
print(params)

nchannels,sampwidth,framerate,nframes = params[:4]
strData = fwav.readframes(nframes)
w= np.fromstring(strData,dtype=np.int16)
w = w*1.0/(max(abs(w)))
w = np.reshape(w,[nframes,nchannels])   #数据转为二维直角坐标



#绘制波形图 第一个声道波形图
time = np.arange(0,nframes)*(1.0 / framerate)
plt.figure()
plt.subplot(5,1,1)
plt.plot(time,w[:,0])
plt.xlabel("Time(s)")
plt.title("First Channel")
plt.show()

#绘制第二个声道的波形图
plt.subplot(5,1,2)
plt.plot(time,w[:,1])
plt.xlabel("Time(s)")
plt.title("Second Channel")

#加大两幅图的距离
plt.subplot(5,1,3)
plt.plot(time,w[:,1])
plt.xlabel("Time(s)")
plt.title("Second Channel")
