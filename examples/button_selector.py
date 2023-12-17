from typing import cast, Callable, Optional, Union
from pydantic import BaseModel
from reactpy import component, html, use_state, event
from reactpy.svg import svg, path
from reactpy_github_buttons import (
    FollowButton, InstallPackageButton, SponsorButton, StarButton, WatchButton,
    ForkButton, IssueButton, DiscussButton, DownloadButton, UseTemplateButton, UseThisGitHubActionButton)


# pylint: disable=line-too-long

from utils.fast_server import run

GIT_USER = 'buttons'
GIT_REPO = 'github-buttons'

class ButtonType(BaseModel):
    button: Callable
    name: str
    repo: bool = False
    large: bool = True
    standard_icon: bool = False
    show_count: bool = False

    @property
    def button_name(self):
        return str(self.button).split(' ')[1]


BUTTON_TYPES = [
    ButtonType(button=FollowButton, name='Follow', show_count=True),
    ButtonType(button=SponsorButton, name='Sponsor',standard_icon=True),
    ButtonType(button=WatchButton, name='Watch', repo=True, show_count=True, standard_icon=True),
    ButtonType(button=StarButton, name='Star', repo=True, show_count=True, standard_icon=True),
    ButtonType(button=ForkButton, name='Fork', repo=True, show_count=True, standard_icon=True),
    ButtonType(button=IssueButton, name='Issue', repo=True, show_count=True, standard_icon=True),
    ButtonType(button=DiscussButton, name='Discuss', repo=True, standard_icon=True),
    ButtonType(button=DownloadButton, name='Download', repo=True, show_count=True, standard_icon=True),
    ButtonType(button=InstallPackageButton, name='Install this package'),
    ButtonType(button=UseTemplateButton, name='Use this template', repo=True, show_count=True, standard_icon=True),
    ButtonType(button=UseThisGitHubActionButton, name='Use this GitHub Action', repo=True, show_count=True, standard_icon=True)
]

class ButtonOptions(BaseModel):
    user: str = GIT_USER
    repo: Optional[str] = None
    large: Optional[bool] = None
    standard_icon: Optional[bool] = None
    show_count: Optional[bool] = None


class Button(BaseModel):
    type: ButtonType
    options: ButtonOptions = ButtonOptions()


def usage_template(button:Button) -> str:

    if button is None:
        return ""

    opt = button.options

    options = []

    options.append(f'user=\"{opt.user}\"')

    if opt.repo:
        options.append(f'repo=\"{opt.repo}\"')

    if opt.large:
        options.append('large=True')

    if opt.standard_icon :
        options.append('standard_icon=True')

    if opt.show_count:
        options.append('show_count=True')

    template = f"""
        from reactpy import component
        from reactpy_github_buttons import {button.type.button_name}

        @component
        def AppMain():
            return {button.type.button_name}({', '.join(options)})

    """
    return ''.join(template.split("        ")[1:])


@component
def AppHeader():
    return html.header({'class_name': 'header user-select-none'},
        html.nav({'class_name': 'navbar navbar-light'},
            html.div({'class_name': 'container px-0'},
                html.a({'class_name': 'navbar-brand mr-auto'},
                    svg({'version': '1.1', 'width': '78.75', 'height': '28', 'viewBox': '0 0 45 16', 'class_name': 'octicon octicon-logo-github', 'aria-label': 'GitHub'},
                        path({'fill-rule': 'evenodd', 'd': 'M18.53 12.03h-.02c.009 0 .015.01.024.011h.006l-.01-.01zm.004.011c-.093.001-.327.05-.574.05-.78 0-1.05-.36-1.05-.83V8.13h1.59c.09 0 .16-.08.16-.19v-1.7c0-.09-.08-.17-.16-.17h-1.59V3.96c0-.08-.05-.13-.14-.13h-2.16c-.09 0-.14.05-.14.13v2.17s-1.09.27-1.16.28c-.08.02-.13.09-.13.17v1.36c0 .11.08.19.17.19h1.11v3.28c0 2.44 1.7 2.69 2.86 2.69.53 0 1.17-.17 1.27-.22.06-.02.09-.09.09-.16v-1.5a.177.177 0 0 0-.146-.18zm23.696-2.2c0-1.81-.73-2.05-1.5-1.97-.6.04-1.08.34-1.08.34v3.52s.49.34 1.22.36c1.03.03 1.36-.34 1.36-2.25zm2.43-.16c0 3.43-1.11 4.41-3.05 4.41-1.64 0-2.52-.83-2.52-.83s-.04.46-.09.52c-.03.06-.08.08-.14.08h-1.48c-.1 0-.19-.08-.19-.17l.02-11.11c0-.09.08-.17.17-.17h2.13c.09 0 .17.08.17.17v3.77s.82-.53 2.02-.53l-.01-.02c1.2 0 2.97.45 2.97 3.88zm-8.72-3.61H33.84c-.11 0-.17.08-.17.19v5.44s-.55.39-1.3.39-.97-.34-.97-1.09V6.25c0-.09-.08-.17-.17-.17h-2.14c-.09 0-.17.08-.17.17v5.11c0 2.2 1.23 2.75 2.92 2.75 1.39 0 2.52-.77 2.52-.77s.05.39.08.45c.02.05.09.09.16.09h1.34c.11 0 .17-.08.17-.17l.02-7.47c0-.09-.08-.17-.19-.17zm-23.7-.01h-2.13c-.09 0-.17.09-.17.2v7.34c0 .2.13.27.3.27h1.92c.2 0 .25-.09.25-.27V6.23c0-.09-.08-.17-.17-.17zm-1.05-3.38c-.77 0-1.38.61-1.38 1.38 0 .77.61 1.38 1.38 1.38.75 0 1.36-.61 1.36-1.38 0-.77-.61-1.38-1.36-1.38zm16.49-.25h-2.11c-.09 0-.17.08-.17.17v4.09h-3.31V2.6c0-.09-.08-.17-.17-.17h-2.13c-.09 0-.17.08-.17.17v11.11c0 .09.09.17.17.17h2.13c.09 0 .17-.08.17-.17V8.96h3.31l-.02 4.75c0 .09.08.17.17.17h2.13c.09 0 .17-.08.17-.17V2.6c0-.09-.08-.17-.17-.17zM8.81 7.35v5.74c0 .04-.01.11-.06.13 0 0-1.25.89-3.31.89-2.49 0-5.44-.78-5.44-5.92S2.58 1.99 5.1 2c2.18 0 3.06.49 3.2.58.04.05.06.09.06.14L7.94 4.5c0 .09-.09.2-.2.17-.36-.11-.9-.33-2.17-.33-1.47 0-3.05.42-3.05 3.73s1.5 3.7 2.58 3.7c.92 0 1.25-.11 1.25-.11v-2.3H4.88c-.11 0-.19-.08-.19-.17V7.35c0-.09.08-.17.19-.17h3.74c.11 0 .19.08.19.17z'})
                    ),
                    html.span({'class_name': 'logo logo-colon'}, ":"),
                    html.span({'class_name': 'logo logo-buttons'}, "buttons")
                ),
                html.ul({'class_name': 'navbar-nav'},
                    html.li({'class_name': 'nav-item'},
                        html.a({'class_name': 'nav-link', 'href': 'https://github.com/buttons/github-buttons'},
                            html.span({'class_name': 'd-none d-sm-inline'}, " View on GitHub"),
                            svg({'version': '1.1', 'width': '16', 'height': '16', 'viewBox': '0 0 16 16', 'class_name': 'octicon octicon-mark-github', 'aria-hidden': 'true'},
                                path({'fill-rule': 'evenodd', 'd': 'M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z'})
                            )
                        )
                    )
                )
            )
        )
    )

@component
def FormContainer(form):
    return html.main({'class_name': 'main'},
    html.div({'class_name': 'container mt-3'},
        html.div({'id': 'app', 'data-v-app': ''},
            html.div({'id': 'app'},
                form
            )
        )
    )
)

@component
def ButtonCheckBox(bt: ButtonType, on_change):
    """Button name & icon, displayed in the top panel"""

    return html.div({'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
        html.div({'class_name': 'form-check'},
            html.label({'class_name': 'form-check-label'},
                html.input({'type': 'radio',
                            'class_name': 'form-check-input', 
                            'name': 'type', 
                            'value': bt.name, 
                            'onchange': lambda evt: on_change(bt)}),
                bt.name,
                html.br(),
                bt.button(large=True)
            )
        )
    )


@component
def UserAndRepo(user_change, repo_change):
    return  html.div({'class_name': 'form-group'},
        html.div({'class_name': 'input-group'},
            html.input({'class_name': 'form-control', 'id': 'user', 'type': 'text', 'maxlength': '39', 'placeholder': ':user', 'autofocus': '', 'onchange': user_change}),
            html.div({'class_name': 'input-group-append input-group-prepend'},
                html.span({'class_name': 'input-group-text'}, "/")
            ),
            html.input({'class_name': 'form-control', 'id': 'repo', 'type': 'text', 'maxlength': '100', 'placeholder': ':repo', 'onchange': repo_change})
        )
    )

@component
def ColorSchemeDropdown(id, disabled):

    select_attr = {'id': id, 'class_name': 'form-control form-control-sm'}

    if disabled:
        select_attr.update({'id': id, 'class_name': 'form-control form-control-sm','disabled': True})

    return html.div({'class_name': 'col-auto'},
        html.label({'class_name': 'sr-only', 'html_for': id}, "@media (prefers-color-scheme: no-preference)"),
        html.select(select_attr,
            html.option({'data-v-3e07ce4a': ''}, "light"),
            html.option({'data-v-3e07ce4a': ''}, "light_high_contrast"),
            html.option({'data-v-3e07ce4a': ''}, "dark"),
            html.option({'data-v-3e07ce4a': ''}, "dark_dimmed"),
            html.option({'data-v-3e07ce4a': ''}, "dark_high_contrast")
        )
    )

@component
def OptionCheckBox(label: str, toggle_state, value: Union[bool, None], enabled:bool):
    """Option large, standard_icon, etc"""

    def is_disabled(attr:dict) -> dict:
        if not enabled:
            attr.update({'disabled': True})
        if value:
            attr.update({'checked': True})
        return attr

    return  html.div({'class_name': 'form-row my-2'},
        html.div({'class_name': 'col-auto'},
            html.div({'class_name': 'form-check'},
                html.label({'class_name': 'form-check-label'},
                    html.input(is_disabled({'class_name': 'form-check-input', 'type': 'checkbox', 'onclick': toggle_state})),
                    label
                )
            )
        )
    )


@component
def example_button(button: Button):
    """Build a live button from the current configuration"""

    if button is None:
        return ""

    args = button.options.dict(exclude_none=True)

    # log.info('%s(%s)', button.type.button_name, args)

    example = button.type.button(**args)
    return example


@component
def AppBody():

    color_scheme_disabled, set_color_scheme_disabled = use_state(True)
    button, set_button = use_state(cast(Button, None))


    # log.info('color_scheme_disabled=%s', color_scheme_disabled)

    # if button:
    #     log.info('button_type="%s", options=%s', button.type.name, button.options)
    # else:
    #     log.info('No button selected')


    @event
    def toggle_color_scheme(event):
        set_color_scheme_disabled(not color_scheme_disabled)

    @event
    def user_change(event):
        value = event['target']['value']
        button.options.user = value
        set_button(button.model_copy())

    @event
    def repo_change(event):
        value = event['target']['value']
        button.options.repo = value
        set_button(button.model_copy())

    @event
    def toggle_large(event):
        button.options.large = None if button.options.large else True
        set_button(button.copy())

    @event
    def toggle_standard_icon(event):
        button.options.standard_icon = None if button.options.standard_icon else True
        set_button(button.copy())

    @event
    def toggle_show_count(event):
        button.options.show_count = None if button.options.show_count else True
        set_button(button.copy())

    def extended_form_hidden(attr:dict) -> dict:
        """Show the Button Options & Preview if a button has been selected"""
        if button is None:
            attr.update({'hidden': True})
        return attr

    def button_select(bt: ButtonType):
        options = ButtonOptions(repo = GIT_REPO if bt.repo else None)
        button = Button(type=bt, options=options)
        set_button(button)

    return FormContainer(
        html.form({'autocapitalize': 'none', 'autocomplete': 'off', 'autocorrect': 'off', 'spellcheck': 'false'},
            html.fieldset({'class_name': 'form-group'},
                html.h4("Choose a button"),
                html.div({'class_name': 'row'},
                    *[ButtonCheckBox(button, on_change=button_select) for button in BUTTON_TYPES]
                ),
            ),
            html.hr(),
            html.div(extended_form_hidden({'class_name': 'row'}),
                html.div({'class_name': 'col-12 col-sm-6 col-md-5'},
                    html.h4("Button options"),
                    UserAndRepo(user_change=user_change, repo_change=repo_change),
                    html.div({'class_name': 'form-group'},
                        html.div({'class_name': 'form-row align-items-center my-1'},
                            html.div({'class_name': 'col-auto mr-auto'},
                                html.div({'class_name': 'form-check'},
                                    html.label({'class_name': 'form-check-label'},
                                        html.input({'class_name': 'form-check-input', 'type': 'checkbox', 'onclick': toggle_color_scheme}),
                                        "Color scheme"
                                    )
                                )
                            ),
                            ColorSchemeDropdown(id='prefers-color-scheme-no-preference', disabled=color_scheme_disabled)
                        ),
                        html.div({'class_name': 'form-row align-items-center my-1 ml-3'},
                            html.div({'class_name': 'col-auto mr-auto'},
                                html.label({'html_for': 'prefers-color-scheme-light', 'class_name': 'form-check-label col-form-label-sm'}, "@media (prefers-color-scheme: light)")
                            ),
                            ColorSchemeDropdown(id='prefers-color-scheme-light', disabled=color_scheme_disabled)
                        ),
                        html.div({'class_name': 'form-row align-items-center my-1 ml-3'},
                            html.div({'class_name': 'col-auto mr-auto'},
                                html.label({'html_for': 'prefers-color-scheme-dark', 'class_name': 'form-check-label col-form-label-sm'}, "@media (prefers-color-scheme: dark)")
                            ),
                            ColorSchemeDropdown(id='prefers-color-scheme-dark', disabled=color_scheme_disabled)
                        ),
                        OptionCheckBox("Large button", toggle_large,
                                        value = button and button.options.large,
                                        enabled = button and button.type.large
                                        ),
                        OptionCheckBox("Show count", toggle_show_count,
                                        value = button and button.options.show_count,
                                        enabled = button and button.type.show_count
                                        ),
                        OptionCheckBox("Standard icon", toggle_standard_icon,
                                        value = button and button.options.standard_icon,
                                        enabled  = button and button.type.standard_icon
                                        ),
                    ),
                    html.div({'class_name': 'form-group'},
                        html.label({'html_for': 'syntax'}, "Syntax"),
                        html.select({'id': 'syntax', 'class_name': 'form-control'},
                            html.option("html"),
                            html.option({'value': 'vue'}, "vue-github-button"),
                            html.option({'value': 'react'}, "react-github-btn")
                        )
                    )
                ),
                html.div({'class_name': 'col-12 col-sm-6 col-md-7'},
                    html.h4("Preview and code"),
                    html.p("Try out your button, then copy and paste the code below into the HTML for your site."),
                    html.p({'style': 'height: 20px;'}, example_button(button)),
                    html.div({'class_name': 'form-group'},
                        html.textarea({'class_name': 'form-control', 'rows': '8', 'readonly': True, 'value': usage_template(button)})
                    )
                )
            )
        )
    )

@component
def AppMain():
    return html._(AppHeader(), AppBody())

# python -m examples.button_selector

if __name__ == "__main__":
    run(AppMain, disable_server_logs=True)
