## Facial_Rec



平台Pycharm，基于python、腾讯云人脸识别API.

需要用到的包tencentcloud-sdk、base64、numpy、cv2、json等

API :
1. 人脸检测与分析API <https://cloud.tencent.com/document/product/867/44989>

> 功能：返回一张图片中是否包含人脸

2. 人员库管理相关接口API <https://cloud.tencent.com/document/product/867/45015>

> 功能：对人员库中未记录的人员进行增加，若人员库中含有该人，则不增加。

3. 人脸搜索

> 功能：用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的一个人员，返回该人员的相似分数，若大于某个值，则说明库中有此人。

视频分帧代码、按帧合成视频代码来自于Internet.

