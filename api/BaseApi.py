import json
import os
import sys
import requests
import yaml
from Wework.api.Wutils import LogRecorder

class BaseApi:
    """
    usage: 封账接口测试需要的公共方法
    :param _params: 用于存储要被替换的变量的值
    """

    _params = dict()
    base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 获取当前目录的父目录绝对路径，用以解决不同环境下能够自动获取路径加强程序的健壮性
    sys.path.append(base_path)
    # 将path环境变量加到sys.path，防止命令行或者shell运行报错

    def send_api(self, apidata: dict):
        """
        usage: 发送请求的公共方法
        :param apidata: 从xxxApi.yaml中读取需要发送的参数
        :return: 返回服务端响应的数据
        """
        apidataStr = yaml.dump(apidata)    # 转化成str
        LogRecorder.logger.debug(f"global _params is {self._params}")   # 要替换的字典值记录日志
        for key, value in self._params.items():
            apidataStr = apidataStr.replace(f"${{{key}}}", str(value))
            # 替换yaml中定义的变量,str的作用是字符串转换，yaml中使用${variableName}表示需要替换的变量，params中key保持和需要替换的variableName一致即可
        apidata = yaml.safe_load(apidataStr)    # 转换成字典
        LogRecorder.logger.info(f"be sending apidata is {apidata}")
        # 发送数据记录日志
        try:
            response = requests.request(
                **apidata)
            # 字典拆包，支持request多个参数扩展写入
            LogRecorder.logger.info(f"origin response is {response.json()}")
            # 返回值记录日志
            return response.json()
        except Exception as e:
            LogRecorder.logger.error(e)
            # 发送失败记录错误日志
        # 使用json，否则展示的值只有《Response200》

    @staticmethod
    def api_decorator(func):
        """
        usage: 针对接口的数据发送流程封装业务接口通用装饰器，1.日志记录收到的测试数据，2.将测试数据加入到_params中替换json下的
               ${data}变量3.获取接口函数名，4.通过接口函数名读取send_api所需的发送参数
        :param func: 业务接口函数名
        :param self: 类方法装饰器
        :param testdata: 从testxxx.yaml中加载的接口字段发送数据
        """
        def inner(self, testdata):
            LogRecorder.logger.info(f"testdata is {testdata}")
            self._params["testdata"] = testdata
            method = func.__name__
            return self.send_api(self._data[method])
        return inner

