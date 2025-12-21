from typing import Any, Callable
from reactpy.testing import DisplayFixture
from examples.all_buttons import AppMain
from .tooling.wait_stable import wait_page_stable


async def test_all_buttons(display: DisplayFixture, assert_snapshot: Callable[[bytes], Any]) -> None:
    await display.show(AppMain)
    await wait_page_stable(display.page)

    assert_snapshot(await display.page.screenshot())
