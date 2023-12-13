from typing import Literal, Union, List, Dict, Any, Optional
from pathlib import Path

from reactpy.web.module import export, module_from_file


_js_module = module_from_file(
    "reactpy_github_buttons",
    file=Path(__file__).parent / "bundle.js",
    fallback="⏳",
)

_RactpyGithubButtons = export(_js_module, "RactpyGithubButtons")


def GithubButton(
        href:Optional[str] =  None,
        data_text:Optional[str] = None,
        data_size:Optional[str] = None,
        data_show_count:Optional[str] = None,
        data_icon:Optional[str] = None,
        data_color_scheme:Optional[str] = None,
        aria_label:Optional[str] = None
        ):
    """ Wrapper for github-buttons library. For API and examples see:

        https://github.com/buttons/github-buttons

    Args:
        chart_type (ChartType): _description_
        width (str,int]): _description_
        height (str,int]): _description_
        series (List[float]): _description_
        options (Dict[str, Any]): _description_

    Returns:
        _type_: _description_
    """

    _args = {
    }

    if href:
        _args['href'] = href

    if data_text:
        _args['data-text'] = data_text

    if data_size:
        _args['data-size'] = data_size

    if data_show_count:
        _args['data-show-count'] = data_show_count

    if data_icon:
        _args['data-icon'] = data_icon

    if data_text:
        _args['data-text'] = data_text

    if data_color_scheme:
        _args['data-color-scheme'] = data_color_scheme

    if aria_label:
        _args['aria-label'] = aria_label


    return _RactpyGithubButtons(_args)
