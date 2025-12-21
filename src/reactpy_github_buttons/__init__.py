# the version is statically loaded by Hatch from pyproject.toml
__version__ = "0.0.19b4"

from .button_wrapper import (
    FollowButton,StarButton,SponsorButton, WatchButton, ForkButton,
    IssueButton, DiscussButton, DownloadButton, InstallPackageButton,
    UseTemplateButton, UseThisGitHubActionButton, make_color_scheme, ColorScheme)

__all__ = [
    "FollowButton",
    "StarButton",
    "SponsorButton",
    "WatchButton",
    "ForkButton",
    "IssueButton",
    "DiscussButton",
    "DownloadButton",
    "InstallPackageButton",
    "UseTemplateButton",
    "UseThisGitHubActionButton",
    "make_color_scheme",
    "ColorScheme",
]
