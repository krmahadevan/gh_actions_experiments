import pytest


@pytest.mark.dependency()
def test_parent():
    print(f"This is parent Test")


@pytest.mark.dependency(depends=["test_parent"])
def test_child():
    print(f"This is child Test")
