#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:22:38 2021

@author: zhangjy
"""

import os

import cv2


def makeVideo(path, size):
    filelist = os.listdir(path)
    filelist.sort(key=lambda x:int(x[:-4]))
    # print(filelist)
    filelist2 = [os.path.join(path, i) for i in filelist]
    print(filelist2)
    fps = 8  # 我设定位视频每秒1帧，可以自行修改
    # size = (1920, 1080)  # 需要转为视频的图片的尺寸，这里必须和图片尺寸一致
    video = cv2.VideoWriter(path + "/Video.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps,
                            size) 

    for item in filelist2:
        print(item)
        if item.endswith('.jpg'):
            print(item)
            img = cv2.imread(item)
            video.write(img)

    video.release()
    cv2.destroyAllWindows()
    print('视频合成生成完成啦')


if __name__ == '__main__':
    path = './source/img'
    # 需要转为视频的图片的尺寸,必须所有图片大小一样，不然无法合并成功
    size = (1592, 884)
    makeVideo(path, size)