import base64
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20200303 import iai_client, models

def create_person(img,name,id):
    base64_data = base64.b64encode(img)
    base64_code = base64_data.decode()
    cred = credential.Credential("XXXXXX", "XXXXXX")  //密钥
    httpProfile = HttpProfile()
    httpProfile.endpoint = "iai.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = iai_client.IaiClient(cred, "ap-shanghai", clientProfile)

    req = models.CreatePersonRequest()
    params = {
        "GroupId": "20210715",
        "PersonName": name,
        "PersonId": id,
        "Gender": 0,
        "Image": base64_code,
        "UniquePersonControl": 2,
        "QualityControl": 0
    }
    req.from_json_string(json.dumps(params))

    resp = client.CreatePerson(req)
    #print(resp.to_json_string())