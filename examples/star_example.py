from reactpy import component, html, run
from utils.logger import log, logging
from reactpy_github_buttons import FollowButton, InstallPackageButton, SponsorButton, StarButton, WatchButton, ForkButton, IssueButton, DiscussButton, DownloadButton

@component
def AppMain():

    # https://buttons.github.io/

    return html.div(
        FollowButton(user='themesberg', repo='tailwind-dashboard-windster'),
        FollowButton(user='themesberg', repo='tailwind-dashboard-windster', show_count=False),
        FollowButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),

        SponsorButton(user='themesberg', repo='tailwind-dashboard-windster'),
        SponsorButton(user='themesberg', repo='tailwind-dashboard-windster', standard_icon=True),
        SponsorButton(user='themesberg', repo='tailwind-dashboard-windster', show_count=False),
        SponsorButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),

        WatchButton(user='themesberg', repo='tailwind-dashboard-windster'),
        WatchButton(user='themesberg', repo='tailwind-dashboard-windster', standard_icon=True),
        WatchButton(user='themesberg', repo='tailwind-dashboard-windster', show_count=False),
        WatchButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),

        StarButton(user='themesberg', repo='tailwind-dashboard-windster'),
        StarButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),
        StarButton(user='themesberg', repo='tailwind-dashboard-windster', large=True, show_count=False),

        ForkButton(user='themesberg', repo='tailwind-dashboard-windster'),
        ForkButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),
        ForkButton(user='themesberg', repo='tailwind-dashboard-windster', large=True, show_count=False),

        IssueButton(user='themesberg', repo='tailwind-dashboard-windster'),
        IssueButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),
        IssueButton(user='themesberg', repo='tailwind-dashboard-windster', large=True, show_count=False),

        DiscussButton(user='themesberg', repo='tailwind-dashboard-windster'),
        DiscussButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),
        DiscussButton(user='themesberg', repo='tailwind-dashboard-windster', standard_icon=True),

        DownloadButton(user='themesberg', repo='tailwind-dashboard-windster'),
        DownloadButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),

        InstallPackageButton(user='themesberg', repo='tailwind-dashboard-windster'),
        InstallPackageButton(user='themesberg', repo='tailwind-dashboard-windster', large=True),

    )

# python -m examples.star_example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
