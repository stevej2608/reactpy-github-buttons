from reactpy import component, html, run
from utils.logger import log, logging
from reactpy_github_buttons import StarButton, make_color_scheme, ColorScheme

GIT_USER = "reactive-python"
GIT_REPO = "reactpy"


@component
def AppMain():
    return html.div(
        StarButton(
            user=GIT_USER,
            repo=GIT_REPO,
            show_count=True,
            color_scheme="no-preference: light_high_contrast; light: light; dark: dark_high_contrast;",
        ),
        StarButton(
            user=GIT_USER,
            repo=GIT_REPO,
            show_count=True,
            color_scheme=make_color_scheme(
                no_preference=ColorScheme.LIGHT_HIGH_CONTRAST,
                light=ColorScheme.LIGHT,
                dark=ColorScheme.DARK_HIGH_CONTRAST,
            ),
        ),
        StarButton(
            user=GIT_USER,
            repo=GIT_REPO,
            show_count=True,
            color_scheme=make_color_scheme(
                no_preference=ColorScheme.LIGHT_HIGH_CONTRAST,
                light=ColorScheme.LIGHT,
                dark=ColorScheme.LIGHT,
            ),
        ),
        StarButton(
            user=GIT_USER,
            repo=GIT_REPO,
            show_count=True,
            color_scheme=make_color_scheme(
                no_preference=ColorScheme.DARK_HIGH_CONTRAST,
                light=ColorScheme.LIGHT_HIGH_CONTRAST,
                dark=ColorScheme.LIGHT,
            ),
        ),
    )


# python -m examples.color_scheme

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
