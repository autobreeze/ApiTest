from Wework.api.FatherApi import FatherApi
from Wework.api.Wutils import Wtool, LogRecorder
class TagApi(FatherApi):

    def __init__(self):
        self._data = Wtool.load_yaml('api/apiData/tagApi.yaml')
        self._params["ip"] = Wtool.load_conf(path=r"conf\env.conf", section="IPADDRESS", option="env_ip")
        # 使用环境的ip可以通过conf\env.conf自定义配置
        self._params["corpsecret"] = self._data["corpsecret"]
        self._params["corpid"] = self._data["corpid"]
        # 将copid和secrete放入字典用于替换，fatherApi.yaml中的${corpid}，${corpsecret}变量
        self._params["access_token"] = self.get_token()

    def create_tag(self, testdata:dict):
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["create_tag"])

    def update_tag(self, testdata:dict):
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["update_tag"])

    def delete_tag(self, testdata:dict):#只有params参数
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["tagid"] = testdata["tagid"]
        return self.send_api(self._data["delete_tag"])

    def get_tag_member(self, testdata:dict):#只有params参数
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["tagid"] = testdata["tagid"]
        return self.send_api(self._data["get_tag_member"])

    def add_tag_member(self, testdata:dict):
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["add_tag_member"])

    def delete_tag_member(self, testdata:dict):
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["delete_tag_member"])

    def get_tag_member_list(self):
        LogRecorder.logger.info(f"not need params")
        # self._params["testdata"] = testdata
        return self.send_api(self._data["get_tag_member_list"])
