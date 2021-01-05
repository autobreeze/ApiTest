import os
from Wework.api.BaseApi import BaseApi
from Wework.api.Wutils import Wtool, LogRecorder


class FatherApi(BaseApi):
    """
    usage: 其他接口的依赖接口，用于获取token
    param _token: 用于存储获取的token值，防止反复请求token
    """
    _token = dict()

    def get_token(self):
        """
        usage: 获取token
        :return: 根据模块返回对应的token值
        """
        apidata = Wtool.load_yaml(r"api/apiData/fatherApi.yaml")["get_token"]
        # todo:自动根据当前路径读取数据
        if "corpsecret" not in self._token.keys():
            response = self.send_api(apidata)
            self._token["corpsecret"] = response["access_token"]
        LogRecorder.logger.debug(f"token is {self._token['corpsecret']}")
        # todo：过期时间为3小时，如果有需要可以通过时间判断是否重新获取token
        return self._token['corpsecret']

