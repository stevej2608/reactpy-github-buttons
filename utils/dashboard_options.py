from reactpy import html

from reactpy.backend.fastapi import Options


PAGE_HEADER_TITLE  = 'ReactPy Dashboard'

GOOGLE_FONTS = {
        'rel': 'preconnect',
        'href': 'https://fonts.googleapis.com'
    }

GOOGLE_STATIC_FONTS = {
        'rel': 'preconnect',
        'href': 'https://fonts.gstatic.com',
        'crossorigin': ''
    }

GOOGLE_CSS = {
        'rel': 'stylesheet',
        'href': 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap'
    }

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

def react(version:str = '17.0.1'):
    # https://cdnjs.com/libraries/react/17.0.1
    return [

        html.script({
            'type': 'text/javascript',
            'src': f'https://cdnjs.cloudflare.com/ajax/libs/react/{version}/umd/react.production.min.js',
            'crossorigin': 'anonymous',
            'referrerpolicy': 'no-referrer'
            }),

        html.script({
            'type': 'text/javascript',
            'src': f'https://cdnjs.cloudflare.com/ajax/libs/react-dom/{version}/umd/react-dom.production.min.js',
            'crossorigin': 'anonymous',
            'referrerpolicy': 'no-referrer'
            }),
    ]

def react_development(version:str = '17.0.1'):
    # https://cdnjs.com/libraries/react/17.0.1
    return [

        html.script({
            'type': 'text/javascript',
            'src': f'https://unpkg.com/react@{version}/umd/react.development.js',
            # 'crossorigin': 'anonymous',
            # 'referrerpolicy': 'no-referrer'
            }),

        html.script({
            'type': 'text/javascript',
            'src': f'https://unpkg.com/react-dom@{version}/umd/react-dom.development.js',
            # 'crossorigin': 'anonymous',
            # 'referrerpolicy': 'no-referrer'
            }),
    ]


DASHBOARD_OPTIONS=Options(
    head=html.head(
        html.meta(META_VIEWPORT),
        html.meta(META_COLOR),
        # html.link(GOOGLE_FONTS),
        # html.link(GOOGLE_STATIC_FONTS),
        # html.link(GOOGLE_CSS),
        html.link(BOOTSTRAP_CSS),
        html.link(GITHUB_BUTTONS_CSS),
        # *react(),
        # *react_development(),
        html.title(PAGE_HEADER_TITLE),
    )
)
