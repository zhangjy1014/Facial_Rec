import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20200303 import iai_client, models
import base64


def search_face(img):
    base64_data = base64.b64encode(img)
    base64_code = base64_data.decode()
    cred = credential.Credential("XXXX", "XXXX")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "iai.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = iai_client.IaiClient(cred, "ap-shanghai", clientProfile)

    req = models.SearchFacesRequest()
    params = {
        "Image": base64_code,
        "GroupIds": [ "20210715" ],
        "MinFaceSize": 24,
        "MaxPersonNum": 1,
        "NeedPersonInfo": 1
    }
    req.from_json_string(json.dumps(params))
    resp = client.SearchFaces(req)
    #print(resp.to_json_string())
    s = json.loads(resp.to_json_string())
    score=s['Results'][0]['Candidates'][0]['Score']
    if score>=80:
        return (s['Results'][0]['Candidates'][0]['PersonName'])


