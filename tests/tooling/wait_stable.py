from typing import Any


async def wait_page_stable(page: Any) -> None:
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("domcontentloaded")
    await page.wait_for_timeout(2000)
