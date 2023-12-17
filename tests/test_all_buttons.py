import pytest
from reactpy.testing import DisplayFixture
from examples.all_buttons import AppMain
from .tooling.wait_stable import wait_page_stable


@pytest.mark.anyio
async def test_all_buttons(display: DisplayFixture):
    await display.show(AppMain)
    await wait_page_stable(display.page)

    await display.page.screenshot(path="tests/screenshots/all_buttons.png")

