import re
import pytest
from playwright.async_api import expect
from reactpy.testing import DisplayFixture
from examples.single import AppMain

async def wait_page_stable(page):
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("domcontentloaded")


def str2int(int_str):
    try:
        if isinstance(int_str, list):
            int_str = int_str[0]
        return int(int_str.replace(',', ''))
    except Exception:
        return -1


@pytest.mark.anyio
async def test_sample_app(display: DisplayFixture):
    await display.show(AppMain)
    await wait_page_stable(display.page)

    # https://playwright.dev/python/docs/locators#locate-by-role

    text = await display.page.locator("span").all_inner_texts()
    assert text[1] == 'Star'

    text = await display.page.locator("a.social-count").all_inner_texts()
    assert str2int(text) > 0
