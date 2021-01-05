import pytest
import sys
from Wework.api.TagApi import TagApi
from Wework.api.ContactsApi import ContactsApi
from Wework.api.Wutils import Wtool, LogRecorder



class TestTag:

    path = r"testcase/caseData/test_tag.yaml"
    casedata = Wtool.load_yaml(path)

    @classmethod
    def setup_class(cls):
        LogRecorder.logger.info(f'******** setup_class begin ********')
        cls.tag = TagApi()
        cls.contact = ContactsApi()

    @pytest.mark.parametrize("testdata", casedata["test_create_tag"])
    def test_create_tag(self, testdata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.tag.create_tag(testdata)
        assert response["errcode"] == 0


    @pytest.mark.parametrize("createdata, updatedata", casedata["test_update_tag"])
    def test_update_tag(self, createdata, updatedata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.tag.create_tag(createdata)
        assert response["errcode"] == 0
        response2 = self.tag.update_tag(updatedata)
        assert response2["errcode"] == 0

    @pytest.mark.parametrize("createdata, deletedata", casedata["test_delete_tag"])
    def test_delete_tag(self, createdata, deletedata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.tag.create_tag(createdata)
        assert response["errcode"] == 0
        response2 = self.tag.delete_tag(deletedata)
        assert response2["errcode"] == 0

    @pytest.mark.parametrize("createdata, getdata", casedata["test_get_tag_member"])
    def test_get_tag_member(self, createdata, getdata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.tag.create_tag(createdata)
        assert response["errcode"] == 0
        response2 = self.tag.get_tag_member(getdata)
        assert response2["errcode"] == 0

    @pytest.mark.parametrize("createdata1, createdata2, adddata", casedata["test_add_tag_member"])
    def test_add_tag_member(self, createdata1, createdata2, adddata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        reponse1 = self.contact.create_member(createdata1)
        assert reponse1["errcode"] == 0
        reponse2 = self.tag.create_tag(createdata2)
        assert reponse2["errcode"] == 0
        reponse3 = self.tag.add_tag_member(adddata)
        assert reponse3["errcode"] == 0

    @pytest.mark.parametrize("createdata1, createdata2, adddata, deletedata", casedata["test_delete_tag_member"])
    def test_delete_tag_member(self, createdata1, createdata2, adddata, deletedata):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        reponse1 = self.contact.create_member(createdata1)
        assert reponse1["errcode"] == 0
        reponse2 = self.tag.create_tag(createdata2)
        assert reponse2["errcode"] == 0
        reponse3 = self.tag.add_tag_member(adddata)
        assert reponse3["errcode"] == 0
        reponse4 = self.tag.delete_tag_member(deletedata)
        assert reponse4["errcode"] == 0

    def test_get_tag_member_list(self):
        LogRecorder.logger.info(f"******** {sys._getframe().f_code.co_name} begin ********")
        response = self.tag.get_tag_member_list()
        assert response["errcode"] == 0
