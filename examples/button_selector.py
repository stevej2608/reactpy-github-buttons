from reactpy import component, html


@component
def AppMainX():
    return html.h1("Hello, world!")


@component
def AppMain():
    return html.main({'class_name': 'main'},
        html.div({'class_name': 'container mt-3'},
            html.div({'id': 'app', 'data-v-app': ''},
                html.div({'data-v-3e07ce4a': '', 'id': 'app'},
                    html.form({'data-v-3e07ce4a': '', 'autocapitalize': 'none', 'autocomplete': 'off', 'autocorrect': 'off', 'spellcheck': 'false'},
                        html.fieldset({'data-v-3e07ce4a': '', 'class_name': 'form-group'},
                            html.h4({'data-v-3e07ce4a': ''}, "Choose a button"),
                            html.div({'data-v-3e07ce4a': '', 'class_name': 'row'},
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'follow'}),
                                            "Follow",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'sponsor'}),
                                            "Sponsor",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'watch'}),
                                            "Watch",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'star'}),
                                            "Star",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'fork'}),
                                            "Fork",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'issue'}),
                                            "Issue",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'discuss'}),
                                            "Discuss",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'download'}),
                                            "Download",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'install this package'}),
                                            "Install this package",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'use this template'}),
                                            "Use this template",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'col-9 col-sm-6 col-md-4 col-lg-2'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                        html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                            html.input({'data-v-3e07ce4a': '', 'type': 'radio', 'class_name': 'form-check-input', 'name': 'type', 'value': 'use this GitHub Action'}),
                                            "Use this GitHub Action",
                                            html.br({'data-v-3e07ce4a': ''}),
                                            html.span({'data-v-3e07ce4a': '', 'aria-hidden': 'true'},
                                                html.span()
                                            )
                                        )
                                    )
                                )
                            )
                        ),
                        html.hr({'data-v-3e07ce4a': ''}),
                        html.div({'data-v-3e07ce4a': '', 'class_name': 'row'},
                            html.div({'data-v-3e07ce4a': '', 'class_name': 'col-12 col-sm-6 col-md-5'},
                                html.h4({'data-v-3e07ce4a': ''}, "Button options"),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'form-group'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'input-group'},
                                        html.input({'data-v-3e07ce4a': '', 'class_name': 'form-control', 'type': 'text', 'maxlength': '39', 'placeholder': ':user', 'autofocus': ''}),
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'input-group-append input-group-prepend'},
                                            html.span({'data-v-3e07ce4a': '', 'class_name': 'input-group-text'}, "/")
                                        ),
                                        html.input({'data-v-3e07ce4a': '', 'class_name': 'form-control', 'type': 'text', 'maxlength': '100', 'placeholder': ':repo'})
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'form-group'},
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-row align-items-center my-1'},
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto mr-auto'},
                                            html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                                html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                                    html.input({'data-v-3e07ce4a': '', 'class_name': 'form-check-input', 'type': 'checkbox'}),
                                                    "Color scheme"
                                                )
                                            )
                                        ),
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto'},
                                            html.label({'data-v-3e07ce4a': '', 'class_name': 'sr-only', 'html_for': 'prefers-color-scheme-no-preference'}, "@media (prefers-color-scheme: no-preference)"),
                                            html.select({'data-v-3e07ce4a': '', 'id': 'prefers-color-scheme-no-preference', 'class_name': 'form-control form-control-sm', 'disabled': ''},
                                                html.option({'data-v-3e07ce4a': ''}, "light"),
                                                html.option({'data-v-3e07ce4a': ''}, "light_high_contrast"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark_dimmed"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark_high_contrast")
                                            )
                                        )
                                    ),
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-row align-items-center my-1 ml-3'},
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto mr-auto'},
                                            html.label({'data-v-3e07ce4a': '', 'html_for': 'prefers-color-scheme-light', 'class_name': 'form-check-label col-form-label-sm'}, "@media (prefers-color-scheme: light)")
                                        ),
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto'},
                                            html.select({'data-v-3e07ce4a': '', 'id': 'prefers-color-scheme-light', 'class_name': 'form-control form-control-sm', 'disabled': ''},
                                                html.option({'data-v-3e07ce4a': ''}, "light"),
                                                html.option({'data-v-3e07ce4a': ''}, "light_high_contrast"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark_dimmed"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark_high_contrast")
                                            )
                                        )
                                    ),
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-row align-items-center my-1 ml-3'},
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto mr-auto'},
                                            html.label({'data-v-3e07ce4a': '', 'html_for': 'prefers-color-scheme-dark', 'class_name': 'form-check-label col-form-label-sm'}, "@media (prefers-color-scheme: dark)")
                                        ),
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto'},
                                            html.select({'data-v-3e07ce4a': '', 'id': 'prefers-color-scheme-dark', 'class_name': 'form-control form-control-sm', 'disabled': ''},
                                                html.option({'data-v-3e07ce4a': ''}, "light"),
                                                html.option({'data-v-3e07ce4a': ''}, "light_high_contrast"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark_dimmed"),
                                                html.option({'data-v-3e07ce4a': ''}, "dark_high_contrast")
                                            )
                                        )
                                    ),
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-row my-2'},
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto'},
                                            html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                                html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                                    html.input({'data-v-3e07ce4a': '', 'class_name': 'form-check-input', 'type': 'checkbox'}),
                                                    "Large button"
                                                )
                                            )
                                        )
                                    ),
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-row my-2'},
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto'},
                                            html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                                html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                                    html.input({'data-v-3e07ce4a': '', 'class_name': 'form-check-input', 'type': 'checkbox'}),
                                                    "Show count"
                                                )
                                            )
                                        )
                                    ),
                                    html.div({'data-v-3e07ce4a': '', 'class_name': 'form-row my-2'},
                                        html.div({'data-v-3e07ce4a': '', 'class_name': 'col-auto'},
                                            html.div({'data-v-3e07ce4a': '', 'class_name': 'form-check'},
                                                html.label({'data-v-3e07ce4a': '', 'class_name': 'form-check-label'},
                                                    html.input({'data-v-3e07ce4a': '', 'class_name': 'form-check-input', 'type': 'checkbox'}),
                                                    "Standard icon"
                                                )
                                            )
                                        )
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'form-group'},
                                    html.label({'data-v-3e07ce4a': '', 'html_for': 'syntax'}, "Syntax"),
                                    html.select({'data-v-3e07ce4a': '', 'id': 'syntax', 'class_name': 'form-control'},
                                        html.option({'data-v-3e07ce4a': ''}, "html"),
                                        html.option({'data-v-3e07ce4a': '', 'value': 'vue'}, "vue-github-button"),
                                        html.option({'data-v-3e07ce4a': '', 'value': 'react'}, "react-github-btn")
                                    )
                                )
                            ),
                            html.div({'data-v-3e07ce4a': '', 'class_name': 'col-12 col-sm-6 col-md-7'},
                                html.h4({'data-v-3e07ce4a': ''}, "Preview and code"),
                                html.p({'data-v-3e07ce4a': ''}, "Try out your button, then copy and paste the code below into the HTML for your site."),
                                html.p({'data-v-3e07ce4a': '', 'style': 'height: 20px;'},
                                    html.span({'data-v-3e07ce4a': ''},
                                        html.span()
                                    )
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'form-group'},
                                    html.textarea({'data-v-2db68b12': '', 'data-v-3e07ce4a': '', 'class_name': 'form-control', 'rows': '2', 'readonly': ''})
                                ),
                                html.div({'data-v-3e07ce4a': '', 'class_name': 'form-group'},
                                    html.textarea({'data-v-2db68b12': '', 'data-v-3e07ce4a': '', 'class_name': 'form-control', 'rows': '2', 'readonly': ''})
                                )
                            )
                        )
                    )
                )
            )
        )
    )
