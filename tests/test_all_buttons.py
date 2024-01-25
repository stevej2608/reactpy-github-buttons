import pytest
from reactpy.testing import DisplayFixture
from examples.all_buttons import AppMain
from .tooling.wait_stable import wait_page_stable


@pytest.mark.anyio
async def test_all_buttons(display: DisplayFixture, assert_snapshot):
    await display.show(AppMain)
    await wait_page_stable(display.page)

    assert_snapshot(await display.page.screenshot())
