from Wework.api.Wutils import LogRecorder
import pytest
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # print('用例执行结果', out)
    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    if report.when == "setup":
        if report.outcome == "passed":
            LogRecorder.logger.info(f'******** {report.outcome} ********')
        else:
            LogRecorder.logger.error(f'******** {report.outcome} ********')
    if report.when == "call":
        if report.outcome == "passed":
            LogRecorder.logger.info(f'******** {report.outcome} ********')
        else:
            LogRecorder.logger.error(f'******** {report.outcome} ********')



# 解决pytest参数化的标题
# def pytest_collection_modifyitems(items):
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid= item.nodeid.encode("utf-8").decode("unicode_escape")
