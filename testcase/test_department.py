import pytest
import sys
from Wework.api.DepartmentApi import DepartmentApi
from Wework.api.Wutils import Wtool, LogRecorder


class TestDepartment:

    path = r"testcase/caseData/test_department.yaml"
    casedata = Wtool.load_yaml(path)

    @classmethod
    def setup_class(cls):
        LogRecorder.logger.info(f'******** setup_class begin ********')
        cls.department = DepartmentApi()

    @pytest.mark.parametrize("testdata", casedata["test_create_department"])
    def test_create_department(self, testdata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.department.create_department(testdata)
        assert response["errcode"] == 0

    @pytest.mark.parametrize("createdata, updatedata", casedata["test_update_department"])
    def test_update_department(self, createdata, updatedata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.department.create_department(createdata)
        assert response["errcode"] == 0
        response2 = self.department.update_department(updatedata)
        assert response2["errcode"] == 0

    @pytest.mark.parametrize("createdata, deletedata", casedata["test_delete_department"])
    def test_delete_department(self, createdata, deletedata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.department.create_department(createdata)
        assert response["errcode"] == 0
        resonse2 = self.department.delete_department(deletedata)
        assert resonse2["errcode"] == 0

    def test_get_department_list(self, testdata=None):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.department.get_department_list(testdata)
        assert response["errcode"] == 0
