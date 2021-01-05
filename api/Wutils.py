import yaml
import logging
# from jsonpath import jsonpath
from logging.handlers import RotatingFileHandler
import json
from pathlib import Path
import os.path
import os
import configparser

class Wtool:
    """
    usage: 定义工具类
    """

    @classmethod
    def load_yaml(cls, path):
        """
        usage: 加载yaml数据
        :param path: 在Wework下的相对路径，比如 api/apiData/xxx.yaml
        :return yamldata: 从yaml文件中加载的数据
        """
        try:
           base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
           # 获取父目录的绝对路径
           absolutely_path = os.path.join(base_path, path)
           # 组装完整的加载数据路径
           with open(absolutely_path, mode='r', encoding='utf-8') as f:
           # 读取中文，r模式+utf-8编码
            yamldata = yaml.safe_load(f)
            return yamldata
        except Exception as e:
            LogRecorder.logger.error(e)


    @classmethod
    def load_conf(cls, path, section, option):
        """
        usage: 加载conf数据
        :param path: 在Wework下的相对路径，比如 conf/xxx.conf
        :return confdata: 从conf文件中加载的数据
        """
        try:
            base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            absolutely_path = os.path.join(base_path, path)
            conf = configparser.ConfigParser()
            conf.read(absolutely_path, encoding="utf-8")
            confdata = conf.get(section, option)
            LogRecorder.logger.debug(f"confdata is {confdata}")
            return confdata
        except Exception as e:
            LogRecorder.logger.info(e)

    @classmethod
    def find_by_jsonpath(cls, response, path):
        """
        usage: 使用jsonpath查找返回的数据
        :param response:  接口返回值
        :param path:  jsonpath查找表达式
        :return: 返回jsonpath查询的值
        """
        return jsonpath(response, path)


    @classmethod
    def format_response(cls, response):
        """
        usage: 格式化response
        :param response: 接口返回值
        ：return: 返回格式化之后的response
        """
        cls.response = response  # 将其赋值给实例变量，方便类中的其他方法调用
        result = json.dumps(json.loads(response.text), indent=2, ensure_ascii=False)
        # todo 数据转换方法
        # print(f"format response data is {result}")
        # todo:加入日志
        return result

class LogRecorder:
    """
    usage: 记录日志，默认日志等级INFO，每个log最大为30M，最多保留10个日志文件
    """

    _base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    _logpath = os.path.join(_base_path, "testlog")
    _level = logging.INFO
    # 日志模块四步走 1.创建logger对象用于调用日志的记录 2.创建formater格式对象，3.创建日志输出对象handler4.设置handler的日志输出格式和日志级别5.将handler加入到logger中
    if Path(_logpath).exists():
        pass
    else:
        os.mkdir(_logpath)
    _path = os.path.join(_logpath, "testcase.log")
    logger = logging.getLogger(__name__)
    logger.setLevel(_level)
    logger.propagate = 0
    formatter = logging.Formatter("%(asctime)s - %(levelname)s-%(funcName)s: %(message)s", "%y-%m-%d %H:%M:%S")
    rollHandler = RotatingFileHandler(_path, maxBytes=30 * 1024, backupCount=10)
    rollHandler.setLevel(_level)
    rollHandler.setFormatter(formatter)
    logger.addHandler(rollHandler)