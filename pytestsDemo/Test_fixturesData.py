import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestDemo2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.getLoggerdemo()
        log.info(dataLoad[0])
        print(dataLoad[0])
        #print(dataLoad[2])
