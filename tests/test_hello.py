from poppy import hello


def test_hello_poppy():
    assert hello.hello_poppy() == "Hello Poppy!"


def test_hello_poppy_types():
    assert isinstance(hello.hello_poppy(), str)
