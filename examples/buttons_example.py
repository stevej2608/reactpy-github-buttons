from reactpy import component, html, run
from utils.logger import log, logging
from reactpy_github_buttons import FollowButton, InstallPackageButton, SponsorButton, StarButton, WatchButton, ForkButton, IssueButton, DiscussButton, DownloadButton


BUTTON_TYPES = [DiscussButton, DownloadButton, FollowButton, 
                ForkButton, InstallPackageButton, IssueButton, 
                SponsorButton, StarButton, WatchButton]

GIT_USER = 'reactive-python'
GIT_REPO = 'reactpy'

@component
def TableHead():
    return html.thead(
        html.th('Function'),
        html.th('Default'),
        html.td('Large'),
        html.th('Std Icon'),
        html.td('Add Counter'),
    )

@component
def ButtonRow(button):

    # Follow does not support an alternative icon 

    if button is not FollowButton:
        button_std_icon = html.td(button(user=GIT_USER, repo=GIT_REPO, standard_icon=True))
    else:
        button_std_icon = 'N/A'

    # Only these buttons support counters

    if button in [FollowButton, SponsorButton, WatchButton, StarButton, ForkButton, IssueButton]:
        button_show_count = html.td(button(user=GIT_USER, repo=GIT_REPO, show_count=True))
    else:
        button_show_count = 'N/A'

    return html.tr(
        html.td(str(button).split(' ')[1] + '()'),
        html.td(button(user=GIT_USER, repo=GIT_REPO)),
        html.td(button(user=GIT_USER, repo=GIT_REPO, large=True)),
        button_std_icon,
        button_show_count,
    )


@component
def ButtonTable():
    rows = [ButtonRow(button) for button in BUTTON_TYPES]
    return html.table(
        TableHead(),
        html.tbody(*rows)
    )


# python -m examples.buttons_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(ButtonTable)
