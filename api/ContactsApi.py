import os
from Wework.api.BaseApi import BaseApi
from Wework.api.FatherApi import FatherApi
from Wework.api.Wutils import Wtool, LogRecorder


class ContactsApi(FatherApi):
    """
    usage: 通讯录管理类，用于编写通讯录所有接口功能
    """


    def __init__(self):
        """
        usage: 用于数据加载的初始化，包括加载通讯录接口所需的发送参数，测试环境ip，以及获取通讯录token
        """
        self._data = Wtool.load_yaml(r'api\apiData\contactsApi.yaml')
        self._params["ip"] = Wtool.load_conf(path=r"conf\env.conf", section="IPADDRESS", option="env_ip")
        # 使用环境的ip可以通过conf\env.conf自定义配置
        self._params["corpsecret"] = self._data["corpsecret"]
        self._params["corpid"] = self._data["corpid"]
        # 将copid和secrete放入字典用于替换，fatherApi.yaml中的${corpid}，${corpsecret}变量
        self._params["access_token"] = self.get_token()

    def create_member(self, testdata: dict):
        """
        usage: 创建通讯录成员
        :param testdata: 从测试用例传过来的用例参数，主要是json发送的各个字段
        :return: 调用send_api进行数据发送并返回服务端响应
        """
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["testdata"] = testdata
        # 为了自定义发送接口的字段多少，在contactsApi.yaml中不定义发送的字段名称而是以${testdata}代替，\
        # 通过用例传入的字段及其数据实现接口关键字段的自由扩展
        return self.send_api(self._data["create_member"])

    def get_member(self, testdata:dict):
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["userid"] = testdata["userid"]
        return self.send_api(self._data["get_member_info"])

    @BaseApi.api_decorator
    def update_member(self):
        pass

    def delete_member(self, testdata:dict):#只有params数据
        LogRecorder.logger.info(f"casetada is {testdata}")
        self._params["userid"] = testdata["userid"]
        return self.send_api(self._data["delete_member"])

    def batch_delete_member(self, testdata:dict):
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["batch_delete_member"])

    def get_dep_member(self, testdata:dict):#只有params数据
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["department_id"] = testdata["department_id"]
        return self.send_api(self._data["get_dep_member"])

    def get_dep_member_detail(self, testdata:dict):#只有params数据
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["department_id"] = testdata["department_id"]
        self._params["fetch_child"] = testdata["fetch_child"]
        return self.send_api(self._data["get_dep_member_detail"])

    def exchange_userid(self, testdata:dict):#只有params数据
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["exchange_userid"])

    def second_verify(self, testdata:dict):#只有params数据
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["userid"] = testdata["userid"]
        return self.send_api(self._data["second_verify"])

    def invite_member(self, testdata:dict):
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["invite_member"])

    def get_join_qrcode(self, testdata:dict):#只有params数据
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["size_type"] = testdata["size_type"]
        return self.send_api(self._data["get_join_qrcode"])

    def get_active_stat(self, testdata:dict):
        LogRecorder.logger.info(f"casedata is {testdata}")
        self._params["testdata"] = testdata
        return self.send_api(self._data["get_active_stat"])

    # @BaseApi.api_decorator
    # def create_member(self, testdata):
    #     pass
