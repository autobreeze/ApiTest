from Wework.api.ContactsApi import ContactsApi
from Wework.api.Wutils import Wtool, LogRecorder
import pytest
import sys
import os

class TestContacts:

    path = r"testcase/caseData/test_contacts.yaml"
    casedata = Wtool.load_yaml(path)

    @classmethod
    def setup_class(cls):
        LogRecorder.logger.info(f'******** setup_class begin ********')
        cls.contacts = ContactsApi()

    @pytest.mark.parametrize("testdata", casedata["test_create_member"])
    def test_create_member(self, testdata: dict):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.contacts.create_member(testdata)
        assert response["errcode"] == 0

    @pytest.mark.parametrize("createdata, getdata", casedata["test_get_member"])
    def test_get_member(self, createdata: dict, getdata: dict):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.contacts.create_member(createdata)
        assert response["errcode"] == 0
        response2 = self.contacts.get_member(getdata)
        assert response2["userid"] == ((self.casedata["test_get_member"][0])[0])["userid"]

    @pytest.mark.parametrize("createdata, updatedata", casedata["test_update_member"])
    def test_update_member(self, createdata: dict, updatedata: dict):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.contacts.create_member(createdata)
        assert response["errcode"] == 0
        response2 = self.contacts.update_member(updatedata)
        assert response2["errcode"] == 0

    @pytest.mark.parametrize("createdata, deletedata", casedata["test_delete_member"])
    def test_delete_member(self, createdata, deletedata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.contacts.create_member(createdata)
        assert response["errcode"] == 0
        response2 = self.contacts.delete_member(deletedata)
        assert response2["errcode"] == 0

    @pytest.mark.parametrize("createdata, deletedata", casedata["test_batch_delete_member"])
    def test_batch_delete_member(self, createdata, deletedata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.contacts.create_member(createdata)
        assert response["errcode"] == 0
        response2 = self.contacts.batch_delete_member(deletedata)
        assert response2["errcode"] == 0

    @pytest.mark.parametrize("testdata", casedata["test_get_dep_member"])
    def test_get_dep_member(self, testdata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.contacts.get_dep_member(testdata)
        assert response["errcode"] == 0

    @pytest.mark.parametrize("testdata", casedata["test_get_dep_member_detail"])
    def test_get_dep_member_detail(self, testdata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.contacts.get_dep_member_detail(testdata)
        assert response["errcode"] == 0









