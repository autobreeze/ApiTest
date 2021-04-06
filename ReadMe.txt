框架优点：
    1.数据驱动：接口发送，pytest参数化
    2.PO封装，装饰器定义模板函数封装，减少代码冗余
    3.日志记录详细，可以自定义调整日志等级
    4.支持测试环境切换，发布环境切换
    5.支持自定义扩展接口发送的字段，比如是否增加proxies，verify等
    6.接口关键字段自由增加，比如用例1传入3个字段数据，用例2传输4个接口字段数据

环境依赖：
开发环境：
    pycharm，python3.6，allure
    安装方式：pycharm使用官网社区版本
             python3.6根据电脑操作系统，进入官网下载
             allure：https://docs.qameta.io/allure/#_installing_a_commandline
             allure window安装：https://blog.csdn.net/chenfei_5201213/article/details/80982929

python依赖库：
    requests==2.24.0
    jsonpath==0.82
    pytest==5.4.3
    allure-pytest==2.8.16
    allure-python-commons==2.8.16
    PyYAML==5.3.1
    pytest-xdist==2.1.0
    pytest-ordering==0.6
    pytest-repeat==0.9.1
    安装方式：运行install.sh脚本

框架构成：
-api

    -BaseApi 用于封装通用接口业务需要使用的模板函数
        -send_api 用于发送接口消息

    -FatherApi（BaseApi） 主要用于编写其他模块需要依赖的接口函数，
        -get_token 此处为获取token

    -ContactsApi（FatherApi） 通讯录接口功能api
        -creat_member 创建用户
        ......

    -其他功能api函数

    -Wutil 主要用于工具函数封装，使用类装饰器@classmethod，考虑到该类中的方法不必实例化
        -jsonpath 查找返回值
        -format 格式化返回值，加载文件
        -load_yaml 加载yaml文件中的数据

    -apiData 用于数据驱动业务功能模块的yaml数据
        -contactsApi.yaml 通讯录接口模块的数据驱动文件
        ......

-testcase

    -test_contacts 通讯录接口测试用例
        -test_create_member 测试通讯录中的添加成员功能
        ......

    -其他模块接口测试用例

    -caseData 存放各模块测试数据的yaml文件
        -test_contacts.yaml 存放通讯录模块数据的yaml
        ......

-conf
    -env.conf 配置测试环境，如果是线上环境则配置成线上ip，测试环境则配置成测试ip

-testlog

    -testcase.log 主要记录yaml，conf数据加载是否成功，接口发送是否成功，测试用例执行是否成功，以及用例执行时的数据传递，能够反映错误所在函数和原因

-report

    -报告：使用pytest 用例文件名 --alluredir=存储路径
           生成html使用 allure generate 存储路径 -o html报告路径 --clean（清除路径中已经有的报告）
           使用allure open -h 127.0.0.1 -p 8883 html报告路径  查看报告




用例执行流程说明：

    用例：
    1.读取testxx.yaml的测试数据并
    2.初始化：FatherApi.get_token（加载api.yaml，变量替换值写入_params）->BaseApi.send_api（替换变量）->requests.request（发送获取token请求）->返回token
    3.用例执行：使用@pytest.mark.parametrize(data)传入数据->test_contacts.TestContacts.test_creat_member->ContactsApi.create_member->
                BaseApi.send_api（替换变量->requests.request（发送获取token请求）->assert 断言
    4.pytest -n auto 多cpu并行执行用例

    报告：
    1.使用pytest 用例文件名 --alluredir=存储路径
    2.生成html使用 pytest generate 存储路径 -o html报告路径 --clean（清除路径中已经有的报告）
    3.使用allure open -h 127.0.0.1 -p 8883 html报告路径  查看报告


    日志：
    1.主要记录yaml，conf数据加载是否成功，接口发送是否成功，测试用例执行是否成功，以及用例执行时的数据传递，能够反映错误所在函数和原因
    2.默认日志等级为INFO，更细的日志使用DEBUG调试，默认不打印
    3.每条用例以及测试装置之间都使用
    ***** setup/用例执行 *****
    testdata（加载失败时写入err，下同）
    apidata
    response
    ***** faile/passed *****


框架构思上的遇到的问题：
    1.如何实现数据驱动：
    --接口发送的数据驱动：使用yaml定义request发送的各个字段，每一个接口发送需要的参数使用yaml定义
    --如何实现测试用例的参数化：使用测试装置@pytest.mark.parametrize()加载yaml中的测试数据
    2.如何解决接口依赖问题：
    比如每一个接口都需要获取当前模块的token，
    --每一个模块的用例在执行时都使用测试装置获取token值并存储在字典中，接口依赖的值使用特定字符${virablename}定义，执行时进行自动替换
    3.如何在不频繁更改send-api的情况下能够通过yaml动态的调整request参数，以及json接口请求字段
    --通过yaml动态的调整request参数:使用字典拆包的方式request(**dict)
    --通过yaml动态的调整json接口请求字段:api的yaml中json不定义具体的字段使用变量代替${testdata}，具体的发送字段和数据放在test的yaml中，读取时放入字典并替换${testdata}
    4.如何实现多环境的切换：
    --在api的yaml中写死header下的host域名，url的域名使用变量${ip}代替，测试/线上环境ip在具体的conf中去定义,通过程序去加载写入_params并替换
    5.如何在使用shell，cmd运行框架时，包的导入路径，数据的加载路径正确
    --包的导入路径问题：使用sys在环境变量的path中加入当前的包路径，python的package下面必须要有__init__.py文件，否则只是一个dir不是一个python包，导入会频繁报错（Wework			   最开始没有__init__.py,将路径加入之后也频繁报错）
    --数据加载的路径问题：使用os获取包当前父目录的绝对路径并使用路径拼接实现数据加载路径的动态调整
    6.如何将用例和用例初始化的结果写入日志：
    --使用pytest的钩子函数获取结果

框架实现过程细节问题：
    1.企业微信返回值默认json格式打印，IDE打印返回值为《Resonpse 200》 解决方法：r.json（）
    2.无-请求字段有很多，发送时最好是可以动态使用，规避方法：放入测试数据中以字典的方式传递参数，在发送时使用dict的update方法更新发送字段
    3.replace函数中被替换的也要为字符串用str（）函数
    4.避免同一个模块反复请求token 方法：将token放入字典中存储，为空时再请求
    5.@pytest.mark.parametrize()如何定义多组数据生成用例 方法：使用[{},{}]j或者[(),()]格式生成
    6.yaml load过程中加载的open对象的数据类型？ 方法：字节流对象
    7.a = dict.update 直接赋值给a时a为None 方法：因为ypdate是一个方法，其返回值是none，正确的做法是直接使用dick.update(dict)
    8.序列化和反序列化？ 方法：python对象和字符串的相符转换
    9.*args，**kwargs，既能打包也能拆包
    10.os.path.join(path, path2)报错nonetype 方法：path2前面不能使用/a/b/c,要使用a/b/c
    11.实现_params字典和${name}替换要将字典的key值和变量的name值相等，才能一一对应替换变量
    12.测试步骤的驱动，使用run_steps封装使用getattr(self,method)直接调用类对应的方法

待完成项：
    1.api接口完善......
    2.测试用例完善，正向，反向......
    3.pytest的其他测试装置应用到用例，confest.py

重要：不管是数据驱动，还是装饰器，或者其他功能函数，封装的基本思路都是不变的写成模板函数，变的使用数据驱动进行维护