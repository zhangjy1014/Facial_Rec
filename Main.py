import json
from PIL import Image, ImageDraw, ImageFont
from tencentcloud.common import credential
from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.iai.v20200303 import iai_client, models
import numpy as np
import os
import base64
import cv2
import search
import create
import person_length


number=person_length.person_num()
video_name='ch15_20210605110000'

filePath = './source/img'
filelist=os.listdir(filePath)
filelist2 = [os.path.join(filePath, i) for i in filelist]

for doc in filelist2:
	print(doc)
	with open(doc, 'rb') as f:
		img=Image.open(doc)
		base64_data = base64.b64encode(f.read())
		base64_code = base64_data.decode()
		img_tmp=cv2.imread(doc)
	try:
		cred = credential.Credential("XXXX", "XXXXX")
		httpProfile = HttpProfile()
		httpProfile.endpoint = "iai.tencentcloudapi.com"

		clientProfile = ClientProfile()
		clientProfile.httpProfile = httpProfile
		client = iai_client.IaiClient(cred, "ap-shanghai", clientProfile)

		req = models.DetectFaceRequest()
		params = {
		"MaxFaceNum": 80,
		"Image": base64_code,
		"FaceAttributesType": "None",
		"MinFaceSize": 34
		}
		req.from_json_string(json.dumps(params))
                
		resp = client.DetectFace(req)
		s=json.loads(resp.to_json_string())
		for i in range(len(s['FaceInfos'])):
			x=s['FaceInfos'][i]['X']
			y=s['FaceInfos'][i]['Y']
			width=s['FaceInfos'][i]['Width']
			height=s['FaceInfos'][i]['Height']
			# print(x)
			# print(y)
			# print(width)
			# print(height)
			# cropped = img[int(y-10):int(y+height+10),int(x-10):int(x+width+10)]
			cropped = img.crop((int(x-10), int(y-10), int(x+width+10), int(y+height+10)))
			width = width+20  # 获取宽度
			height = height+20  # 获取高度
			if height<64 or width<64:
				cropped = cropped.resize((int(width * 2.7), int(height * 2.7)), Image.ANTIALIAS)
			# cv2.imwrite("D:\\source\\jt\\"+(str(i))+".jpg", cropped)
			cropped.save("./source/jt/"+(str(i))+".jpg")
			with open("./source/jt/"+(str(i))+".jpg", 'rb') as k:
				create.create_person(k.read(),str(number+i),video_name+'_'+str(number+i))
			with open("./source/jt/" + (str(i)) + ".jpg", 'rb') as k:
				person_name=search.search_face(k.read())
				#cv2.rectangle(img_tmp, (int(x-10),int(y-10)), (int(x+width+10),int(y+height+10)), (255,0,0), 4)
				draw = ImageDraw.Draw(img)
				draw.rectangle(((int(x-10),int(y-10)), (int(x+width-10),int(y+height-10))), fill=None, outline='red', width=5)
				font = ImageFont.truetype("simhei.ttf", 40, encoding="utf-8")
				draw.text((int(x+width/2-20), int(y-10) - 40), person_name, (255, 0, 0), font=font)
				cv2charimg = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
				cv2.imwrite("./source/img/"+(str(i+1))+".jpg",cv2charimg)
	except Exception as e:
		print('ededede')
		pass
	continue