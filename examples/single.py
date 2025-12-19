from reactpy import html, component, use_state
from reactpy_github_buttons import StarButton

from utils.app_runner import pico_runner


@component
def AppMain():
    count, set_count = use_state(0)

    def on_click():
        set_count(count + 1)

    return html.div(
        html.h2(f"Button test {count}"),
        StarButton(
            user="buttons",
            repo="github-buttons",
            large=True,
            show_count=True,
            color_scheme="dark",
        ),
        html.button(
            {"class_name": "btn btn-secondary", 'type': 'button', "onClick": lambda e: on_click()},
            'Click Me'
        ),
    )


# python -m examples.single

if __name__ == "__main__":
    pico_runner(AppMain)
