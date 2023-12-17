import pytest
from reactpy.testing import DisplayFixture
from examples.all_buttons import AppMain

async def wait_page_stable(page):
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("domcontentloaded")


@pytest.mark.anyio
async def test_sample_app(display: DisplayFixture):
    await display.show(AppMain)
    await wait_page_stable(display.page)

    await display.page.screenshot(path="tests/screenshots/all_buttons.png")

