from typing import Literal, Union, List, Dict, Any, Optional
from pathlib import Path

from reactpy.web.module import export, module_from_file

# pylint: disable=missing-function-docstring
# pylint: disable=disable=invalid-name

_js_module = module_from_file(
    "reactpy_github_buttons",
    file=Path(__file__).parent / "bundle.js",
    fallback="⏳",
)

_RactpyGithubButtons = export(_js_module, "RactpyGithubButtons")


def GithubButton(user:str, repo:str, props:dict):
    """ Wrapper for github-buttons library. For API and examples see:

        https://github.com/buttons/github-buttons
    """

    _args = {
        'href' : f'https://github.com/{user}/{repo}',
        **props
    }

    if 'text' in props:
        _args['data_text'] = props['text']

    return _RactpyGithubButtons(_args)


def FollowButton(user:str, large=False, show_count=False):

    props = {
        "text" : "Follow @buttons",
        "aria-label": "Follow @buttons on GitHub",
        'href' : f'https://github.com/{user}'
    }

    if large:
        props.update({"data-size": "large"})

    if show_count:
        props.update({"data-show-count": "true"})


    return GithubButton(user=user, repo='', props=props)


def SponsorButton(user:str, large=False, standard_icon=False):

    props = {
        "text" : "Sponsor",
        "aria-label": "Sponsor @buttons on GitHub",
        'href' : f'https://github.com/sponsors/{user}',
    }

    if large:
        props.update({"data-size": "large"})

    if not standard_icon:
        props.update({"data-icon": "octicon-heart"})

    return GithubButton(user=user, repo='', props=props)


def WatchButton(user:str, repo:str, large=False, show_count=False, standard_icon=False):

    props = {
        "text" : "Watch",
        "aria-label": "Watch buttons/github-buttons on GitHub",
        'href' : f'https://github.com/{user}/{repo}/subscription'
    }

    if large:
        props.update({"data-size": "large"})

    if show_count:
        props.update({"data-show-count": "true"})

    if not standard_icon:
        props.update({"data-icon": "octicon-eye"})

    return GithubButton(user=user, repo=repo, props=props)


def StarButton(user:str, repo:str, large=False, show_count=False, standard_icon=False):

    props = {
        "text" : "Star",
        "aria-label": "Star buttons/github-buttons on GitHub",
    }

    if large:
        props.update({"data-size": "large"})

    if show_count:
        props.update({"data-show-count": "true"})

    if not standard_icon:
        props.update({"data-icon": "octicon-star"})

    return GithubButton(user=user, repo=repo, props=props)


def ForkButton(user:str, repo:str, large=False, show_count=False, standard_icon=False):

    props = {
        "text" : "Fork",
        "aria-label": "Fork buttons/github-buttons on GitHub",
        'href' : f'https://github.com/{user}/{repo}/fork'
    }

    if large:
        props.update({"data-size": "large"})

    if show_count:
        props.update({"data-show-count": "true"})

    if not standard_icon:
        props.update({"data-icon": "octicon-repo-forked"})

    return GithubButton(user=user, repo=repo, props=props)


def IssueButton(user:str, repo:str, large=False, show_count=False, standard_icon=False):

    props = {
        "text" : "Issue",
        "aria-label": "Issue buttons/github-buttons on GitHub",
        'href' : f'https://github.com/{user}/{repo}/issues'
    }

    if large:
        props.update({"data-size": "large"})

    if show_count:
        props.update({"data-show-count": "true"})

    if not standard_icon:
        props.update({"data-icon": "octicon-issue-opened"})

    return GithubButton(user=user, repo=repo, props=props)


def DiscussButton(user:str, repo:str, large=False, standard_icon=False):

    props = {
        "text" : "Discuss",
        "aria-label": "Discuss buttons/github-buttons on GitHub",
    }

    if large:
        props.update({"data-size": "large"})

    if not standard_icon:
        props.update({"data-icon": "octicon-comment-discussion"})

    return GithubButton(user=user, repo=repo, props=props)


def DownloadButton(user:str, repo:str, large=False, standard_icon=False):

    props = {
        "text" : "Download",
        "aria-label": "Download buttons/github-buttons on GitHub",
    }

    if large:
        props.update({"data-size": "large"})

    if not standard_icon:
        props.update({"data-icon": "octicon-download"})

    return GithubButton(user=user, repo=repo, props=props)


def InstallPackageButton(user:str, repo:str, large=False, standard_icon=False):

    props = {
        "text" : "Install this package",
        "aria-label": "Install this package buttons/github-buttons on GitHub",
    }

    if large:
        props.update({"data-size": "large"})

    if not standard_icon:
        props.update({"data-icon": "octicon-package"})

    return GithubButton(user=user, repo=repo, props=props)


def UseTemplateButton(user:str, repo:str, large=False, standard_icon=False):

    props = {
        "text" : "Use this template",
        "aria-label": "Use this template buttons/github-buttons on GitHub",
    }

    if large:
        props.update({"data-size": "large"})

    if not standard_icon:
        props.update({"data-icon": "octicon-repo-template"})

    return GithubButton(user=user, repo=repo, props=props)


def UseThisGitHubActionButton(user:str, repo:str, large=False, standard_icon=False):

    props = {
        "text" : "Use this GitHub Action",
        "aria-label": "Use this GitHub Action buttons/github-buttons on GitHub",
    }

    if large:
        props.update({"data-size": "large"})

    if not standard_icon:
        props.update({"data-icon": "octicon-play"})

    return GithubButton(user=user, repo=repo, props=props)
