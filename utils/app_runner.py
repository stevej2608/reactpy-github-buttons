"""
ReactPy v2 compatible run() and pico_runner() functions

This module provides run() and pico_runner() functions for running ReactPy components
with automatic server setup, similar to ReactPy v1 behavior.
"""

import sys
from typing import Any, Callable, List, Optional

import uvicorn
from reactpy import component, html
from reactpy.core.component import Component
from reactpy.types import VdomDict
from reactpy.executors.asgi import ReactPy


def run(
    app_main: Callable[..., Component],
    host: str = "127.0.0.1",
    port: int = 8000,
    title: str = "ReactPy Forms",
    head: Optional[VdomDict] = None,
    **kwargs: Any,
) -> None:
    """Run a ReactPy component with automatic server setup.

    This function provides ReactPy v1-like run() behavior by automatically
    creating and configuring an ASGI server to run your ReactPy component.

    Args:
        app_main: A ReactPy component function decorated with @component
        host: Server host address (default: "127.0.0.1")
        port: Server port (default: 8000)
        title: Page title (default: "ReactPy Forms")
        head: Optional HTML head VdomDict element with additional head content
        **kwargs: Additional arguments passed to uvicorn.run()

    Example:
        ```python
        from reactpy import component, html
        from utils.app_runner import run

        @component
        def AppMain():
            return html.h1("Hello ReactPy!")

        if __name__ == "__main__":
            run(AppMain)
        ```
    """

    # Build head element
    if head is None:
        head = html.head(html.title(title))
    elif "children" in head:
        # Add title to existing head if not present
        children = list(head.get("children", []))
        has_title = any(
            child.get("tagName") == "title"
            for child in children
            if isinstance(child, dict)
        )
        if not has_title:
            children.insert(0, html.title(title))
            head["children"] = children
    else:
        head["children"] = [html.title(title)]

    # Create ReactPy ASGI app
    app = ReactPy(app_main, html_head=head)

    # Display startup message
    print(f"Starting ReactPy server at http://{host}:{port}")
    print("Press CTRL+C to quit")

    try:
        # Run the server
        uvicorn.run(app, host=host, port=port, **kwargs)
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as ex:
        print(f"Server error: {ex}")
    finally:
        sys.exit(0)


def pico_runner(
    app: Callable[..., Component],
    host: str = "127.0.0.1",
    port: int = 8000,
    title: str = "ReactPy Forms",
    additional_head: Optional[List[str]] = None,
    **kwargs: Any,
) -> None:
    """Run a ReactPy component wrapped in a Pico CSS container.

    This function wraps the provided component in a Pico CSS styled container
    and automatically includes the Pico CSS framework in the page head.

    Args:
        app: A ReactPy component function decorated with @component
        host: Server host address (default: "127.0.0.1")
        port: Server port (default: 8000)
        title: Page title (default: "ReactPy Forms")
        additional_head: Optional list of CSS file paths to include
        **kwargs: Additional arguments passed to run()

    Example:
        ```python
        from reactpy import component, html
        from utils.app_runner import pico_runner

        @component
        def AppMain():
            return html.h1("Hello with Pico CSS!")

        if __name__ == "__main__":
            pico_runner(AppMain, additional_head=["assets/css/custom.css"])
        ```
    """

    # Build the head with Pico CSS
    pico_css = html.link({
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css',
        'crossorigin': 'anonymous'
    })

    head_children = [pico_css]

    # Add any additional CSS files
    if additional_head:
        for css_path in additional_head:
            if css_path.endswith('.css'):
                head_children.append(html.link({'rel': 'stylesheet', 'href': css_path}))

    head = html.head(*head_children)

    # Wrap the app in a Pico CSS container
    @component
    def PicoContainer():
        return html.div(
            {'class': "container"},
            html.section(app())
        )

    # Call the generic run() function
    run(PicoContainer, host=host, port=port, title=title, head=head, **kwargs)


def bootstrap_runner(
    app: Callable[..., Component],
    host: str = "127.0.0.1",
    port: int = 8000,
    title: str = "ReactPy GitHub Buttons",
    additional_head: Optional[List[str]] = None,
    **kwargs: Any,
) -> None:
    """Run a ReactPy component with Bootstrap CSS and GitHub Buttons styling.

    This function includes Bootstrap CSS, GitHub Buttons CSS, and appropriate
    meta tags for responsive design.

    Args:
        app: A ReactPy component function decorated with @component
        host: Server host address (default: "127.0.0.1")
        port: Server port (default: 8000)
        title: Page title (default: "ReactPy GitHub Buttons")
        additional_head: Optional list of CSS file paths to include
        **kwargs: Additional arguments passed to run()

    Example:
        ```python
        from reactpy import component, html
        from utils.app_runner import bootstrap_runner

        @component
        def AppMain():
            return html.h1("Hello with Bootstrap!")

        if __name__ == "__main__":
            bootstrap_runner(AppMain)
        ```
    """

    # Build the head with Bootstrap and GitHub Buttons CSS
    meta_viewport = html.meta({
        'name': 'viewport',
        'content': 'width=device-width',
        'initial-scale': 1
    })

    meta_color = html.meta({
        'name': 'theme-color',
        'content': '#000000'
    })

    bootstrap_css = html.link({
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css'
    })

    github_buttons_css = html.link({
        'rel': 'stylesheet',
        'href': 'https://buttons.github.io/css/app.48c6bc16.css'
    })

    head_children = [meta_viewport, meta_color, bootstrap_css, github_buttons_css]

    # Add any additional CSS files
    if additional_head:
        for css_path in additional_head:
            if css_path.endswith('.css'):
                head_children.append(html.link({'rel': 'stylesheet', 'href': css_path}))

    head = html.head(*head_children)

    # Call the generic run() function
    run(app, host=host, port=port, title=title, head=head, **kwargs)

