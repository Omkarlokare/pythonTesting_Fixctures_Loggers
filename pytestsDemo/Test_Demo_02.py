# Any pytest file should  start with test_ or it can end with _test
# pytest method name should start with test
# Any code should be wrapped in method only
# Each method is treated as single test case
# Method name should have sense
# -k stands for method name execution, -s logs in output, -v stands for more info metadata
# You can run a specific file with command -> py.test with file name/path
# You can mark (Tag) tests with @pytest.mark.smoke and then run with -m
# You can skip test with @pytest.mark.skip
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string do not match "


def test_secondCreditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition not match"

