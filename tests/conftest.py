import pytest
from playwright.async_api import async_playwright
from reactpy.testing import DisplayFixture, BackendFixture

pytest_plugins = "tests.tooling.pytest_playwright_visual"

@pytest.fixture(scope="session")
def anyio_backend():
    return 'asyncio'

def pytest_addoption(parser) -> None:
    parser.addoption(
        "--headed",
        dest="headed",
        action="store_true",
        help="Open a browser window when runnging web-based tests",
    )

@pytest.fixture(scope="session")
async def display(server, browser):
    async with DisplayFixture(server, browser) as display:
        yield display


@pytest.fixture(scope="session")
async def server():
    async with BackendFixture() as server:
        yield server


@pytest.fixture(scope="session")
async def browser(pytestconfig):
    async with async_playwright() as pw:
        yield await pw.chromium.launch(headless=not bool(pytestconfig.option.headed))
