import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
# yield is used to tear down the execution of the code written after yield statement.
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("Im creating a data to load")
    return ["Omkar", "Lokare", "omkarlokare.com"]


@pytest.fixture(params=[("chrome", "Omkar", "Lokare"), ("Firefox", "Lokare"),("Edge", "OS")])
def crossBrowser(request):
        return request.param
