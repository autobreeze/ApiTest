from Wework.api.FatherApi import FatherApi
from Wework.api.Wutils import Wtool
from Wework.api.Wutils import Wtool, LogRecorder


class DepartmentApi(FatherApi):

    def __init__(self):
        self._data = Wtool.load_yaml(r'api\apiData\deparmentApi.yaml')
        self._params["ip"] = Wtool.load_conf(path=r"conf\env.conf", section="IPADDRESS", option="env_ip")
        # 使用环境的ip可以通过conf\env.conf自定义配置
        self._params["corpsecret"] = self._data["corpsecret"]
        self._params["corpid"] = self._data["corpid"]
        # 将copid和secrete放入字典用于替换，fatherApi.yaml中的${corpid}，${corpsecret}变量
        self._params["access_token"] = self.get_token()

    def create_department(self, testdata: dict):
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["create_department"])

    def update_department(self, testdata:dict):
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["update_department"])

    def delete_department(self, testdata:dict):#只有params参数
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["id"] = testdata["id"]
        return self.send_api(self._data["delete_department"])

    def get_department_list(self, testdata:dict):#只有params参数
        LogRecorder.logger.info(f"casetada is {testdata}")
        # self._params["testdata"] = testdata
        return self.send_api(self._data["get_department_list"])

