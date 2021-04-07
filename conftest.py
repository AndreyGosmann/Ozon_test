import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--window-size=1900,1050")
    return chrome_options
