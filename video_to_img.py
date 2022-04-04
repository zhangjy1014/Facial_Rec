import time

import cv2
import numpy as np

if __name__ == "__main__":
    threshold = [0.5, 0.6, 0.7]
    cap = cv2.VideoCapture("./source/video/ch15_20210605110000.mp4")
    fps1 = cap.get(cv2.CAP_PROP_FPS)
    i=1
    print(fps1)
    while True:
        t1 = time.time()
        # 从摄像头读取图片
        success, img = cap.read()
        if not success:
            break
        # img = cv2.flip(img, 1)
        temp_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #-------------------------------------#
        #   将图片传入并检测
        #-------------------------------------#
##        rectangles = model.detectFace(temp_img, threshold)

        draw = img.copy()

        t2 = time.time()
        fps = int(1. / (t2 - t1))
        print('fps is: ', fps)
        position = (int(0.25 * draw.shape[0]), int(0.25 * draw.shape[1]))
        #cv2.putText(draw, "FPS:{}".format(fps), position, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        cv2.imshow("test", draw)
        cv2.imwrite("./source/img/"+str(i)+'.jpg', draw)
        i=i+1
        k = cv2.waitKey(1)
        # size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        # out = cv2.VideoWriter('camera_test.avi', cap, fps, size)