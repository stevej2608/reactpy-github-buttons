from reactpy import html
from reactpy.backend.fastapi import Options

PAGE_HEADER_TITLE  = 'ReactPy GitHub Buttons'

BOOTSTRAP_CSS = {
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css'
    }

GITHUB_BUTTONS_CSS = {
        'rel': 'stylesheet',
        'href': 'https://buttons.github.io/css/app.48c6bc16.css'
    }

META_VIEWPORT = {
    'name': "viewport",
    'content': "width=device-width",
    'initial-scale': 1
    }

META_COLOR = {
    'theme-color': "viewport",
    'content': "#000000"
    }

SERVER_OPTIONS=Options(
    head=html.head(
        html.meta(META_VIEWPORT),
        html.meta(META_COLOR),
        html.link(BOOTSTRAP_CSS),
        html.link(GITHUB_BUTTONS_CSS),
        html.title(PAGE_HEADER_TITLE),
    )
)
