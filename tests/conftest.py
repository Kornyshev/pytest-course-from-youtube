import pytest


def pytest_configure(config):
    """Вызывается при конфигурации pytest перед запуском тестов."""
    print("Configuring pytest")


def pytest_unconfigure(config):
    """Вызывается после завершения всех тестов."""
    print("Unconfiguring pytest")


def pytest_runtest_setup(item):
    """Вызывается перед запуском каждого теста."""
    print(f"Setting up test: {item}")


def pytest_runtest_teardown(item, nextitem):
    """Вызывается после завершения каждого теста."""
    print(f"Tearing down test: {item}")


def pytest_sessionstart(session):
    """Вызывается при запуске тестовой сессии."""
    print("Starting test session")


def pytest_sessionfinish(session, exitstatus):
    """Вызывается при завершении тестовой сессии."""
    print("\nFinishing test session")


def pytest_collection_modifyitems(items):
    """Изменяет тестовые элементы перед выполнением."""
    for item in items:
        if "modify" in item.keywords:
            item.add_marker(pytest.mark.skip(reason="Test modified to be skipped"))


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    """Вызывается непосредственно перед вызовом тестовой функции."""
    if "modify" in item.keywords:
        print(f"Modifying test: {item}")


def pytest_addoption(parser):
    parser.addoption("--custom-option", action="store", default="default_value", help="Custom option for pytest")


@pytest.fixture
def custom_option(request):
    return request.config.getoption("--custom-option")
