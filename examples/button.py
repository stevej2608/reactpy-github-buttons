from reactpy import component, html, run
from utils.logger import log, logging
from reactpy_github_buttons import SponsorButton

GIT_USER = 'reactive-python'
GIT_REPO = 'reactpy'


@component
def AppMain():
    return html.div(
        # SponsorButton(user=GIT_USER),
        # SponsorButton(user=GIT_USER, large=True),
        # SponsorButton(user=GIT_USER, standard_icon=True),
        SponsorButton(user=GIT_USER, show_count=True),

    )


# python -m examples.button

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
