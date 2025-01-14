# Any pytest file should  start with test_ or it can end with _test
# pytest method name should start with test
# Any code should be wrapped in method only
# Each method is treated as single test case
# Method name should have sense
# -k stands for method name execution, -s logs in output, -v stands for more info metadata
# You can run a specific file with command -> py.test with file name/path
# You can mark (Tag) tests with @pytest.mark.smoke and then run with -m
# You can skip test with @pytest.mark.skip
# fixtures are used as setup and tear down methods for test cases- conftest file to generalize
# fixtures and make it available to all test cases ( fixture name into parameters of method
# datadriven and parameterization can be done with return statements in tuple format
# When you define fixture scope to class only, it will run once before class is initiated and at the end
# Command to generate Report -> py.test --html=report.html
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print('hello')


@pytest.mark.xfail
def test_secondgreetingCreditcard():
    print('Welcome')


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
