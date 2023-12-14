from reactpy import component, html, run
from utils.logger import log, logging
from reactpy_github_buttons import FollowButton, InstallPackageButton, SponsorButton, StarButton, WatchButton, ForkButton, IssueButton, DiscussButton, DownloadButton


BUTTON_TYPES = [FollowButton, ForkButton, IssueButton, StarButton,
                WatchButton,
                InstallPackageButton, DiscussButton, DownloadButton, SponsorButton]

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

    if button is FollowButton:
        default = html.td(button(user=GIT_USER))
        large = html.td(button(user=GIT_USER, large=True))
        std_icon = 'N/A'
        counter = html.td(button(user=GIT_USER, show_count=True))

    elif button is SponsorButton:
        default = html.td(button(user=GIT_USER))
        large = html.td(button(user=GIT_USER, large=True))
        std_icon = html.td(button(user=GIT_USER, standard_icon=True))
        counter = 'N/A'

    elif button in [WatchButton, StarButton, ForkButton, IssueButton]:
        default = html.td(button(user=GIT_USER, repo=GIT_REPO))
        large = html.td(button(user=GIT_USER, repo=GIT_REPO, large=True))
        std_icon = html.td(button(user=GIT_USER, repo=GIT_REPO, standard_icon=True))
        counter = html.td(button(user=GIT_USER, repo=GIT_REPO, show_count=True))

    else:
        default = html.td(button(user=GIT_USER, repo=GIT_REPO))
        large = html.td(button(user=GIT_USER, repo=GIT_REPO, large=True))
        std_icon = html.td(button(user=GIT_USER, repo=GIT_REPO, standard_icon=True))
        counter = 'N/A'

    return html.tr(
        html.td(str(button).split(' ')[1] + '()'),
        default,
        large,
        std_icon,
        counter,
    )


@component
def ButtonTable():
    rows = [ButtonRow(button) for button in BUTTON_TYPES]
    return html.table(
        TableHead(),
        html.tbody(*rows)
    )

