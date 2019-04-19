'''
之前我们保存图片用的是cv2.imwrite()，要保存视频，我们需要创建一个VideoWriter的对象，需要给它传入四个参数：

 输出的文件名，如’output.avi’
 编码方式FourCC码
 帧率FPS
 要保存的分辨率大小

 FourCC是用来指定视频编码方式的四字节码，所有的编码可参考Video Codecs。
 如MJPG编码可以这样写： cv2.VideoWriter_fourcc(*'MJPG')或cv2.VideoWriter_fourcc('M','J','P','G')
 '''
 import cv2

 capture = cv2.VideoCapture(0)

 # 定义编码方式并创建VideoWriter对象
 fourcc = cv2.VideoWriter_fourcc(*'MJPG')
 outfile = cv2.VideoWriter('output.avi', fourcc, 25.,(640, 480))

 while(capture.isOpened()):
     ret, frame = capture.read()

     if ret:
         outfile.write(frame) # 写入文件
         cv2.imshow('frame', frame)
         if cv2.waitKey(1) == ord('q'):
             break
    else:
        break