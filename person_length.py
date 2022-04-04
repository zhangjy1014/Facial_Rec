import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20200303 import iai_client, models

def person_num():
    cred = credential.Credential("XXXXX", "XXXX")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "iai.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = iai_client.IaiClient(cred, "ap-shanghai", clientProfile)

    req = models.GetPersonListNumRequest()
    params = {
        "GroupId": "20210715"
    }
    req.from_json_string(json.dumps(params))

    resp = client.GetPersonListNum(req)
    s = json.loads(resp.to_json_string())
    return (s['PersonNum'])